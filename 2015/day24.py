import os
import numpy as np
import copy
from collections import defaultdict
import networkx as nx
import sympy
import heapq
import sys
import math
import itertools
import aoctools
from BaseSolver import BaseSolver
from aocd.models import Example

class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

    def get_examples(self):
        examples = []
        examples.append(Example(input_data='''1
2
3
4
5
7
8
9
10
11''', answer_a='99', answer_b='44'))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        weights = []
        for d in data:
            weights.append(int(d))
        weights.reverse()
        weightsum = sum(weights)
        maxweight = max(weights)
        targetweight = weightsum // 3
        if part2:
            targetweight = weightsum // 4
        minlen = 100000000000000000
        minqe = 100000000000000000
        def dfs3(subset1, subset2, subset3, remains):
            nonlocal minlen
            nonlocal targetweight
            nonlocal minqe
            if len(subset1) > minlen or (len(subset1) == minlen and minqe <= np.prod(subset1)):
                return
            if remains == []:
                minlen = len(subset1)
                minqe = np.prod(subset1)
                print(subset1)
                print(f'New minlen: {minlen}, minqe: {minqe}')
                return
            w = remains[0]
            result = []
            if sum(subset1) + w <= targetweight:
                dfs3(subset1 + [w], subset2, subset3, remains[1:])
            if sum(subset2) + w <= targetweight:
                dfs3(subset1, subset2 + [w], subset3, remains[1:])
            if sum(subset3) + w <= targetweight:
                dfs3(subset1, subset2, subset3 + [w], remains[1:])
        def dfs4(subset1, subset2, subset3, subset4, remains):
            nonlocal minlen
            nonlocal targetweight
            nonlocal minqe
            if len(subset1) > minlen or (len(subset1) == minlen and minqe <= np.prod(subset1)):
                return
            if remains == []:
                minlen = len(subset1)
                minqe = np.prod(subset1)
                print(subset1)
                print(f'New minlen: {minlen}, minqe: {minqe}')
                return
            w = remains[0]
            if sum(subset1) + w <= targetweight:
                dfs4(subset1 + [w], subset2, subset3, subset4, remains[1:])
            if sum(subset2) + w <= targetweight:
                dfs4(subset1, subset2 + [w], subset3, subset4, remains[1:])
            if sum(subset3) + w <= targetweight and len(remains) < len(weights):
                dfs4(subset1, subset2, subset3 + [w], subset4, remains[1:])
            if sum(subset4) + w <= targetweight and len(remains) < len(weights) - 1:
                dfs4(subset1, subset2, subset3, subset4 + [w], remains[1:])
        if part2:
            dfs4([], [], [], [], weights)
        else:
            dfs3([], [], [], weights)
        return str(minqe)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
