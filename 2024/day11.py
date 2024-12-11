import os
import numpy as np
import copy
import collections
import networkx as nx
import sympy
import heapq
import sys
import math
import itertools
from aoctools import *
from BaseSolver import BaseSolver
from aocd.models import Example

class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

    def get_examples(self):
        examples = []
        examples.append(Example(input_data='''125 17''', answer_a='55312', answer_b=None))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        stones = []
        for d in data[0].split():
            stones.append(int(d))
        num = 25
        if part2:
            num = 75
        count = collections.Counter(stones)
        for i in range(num):
            newcount = collections.Counter()
            for s, c in count.items():
                st = str(s)
                if s == 0:
                    newcount[1] += c
                elif len(st) % 2 == 0:
                    newcount[int(st[:len(st)//2])] += c
                    newcount[int(st[len(st)//2:])] += c
                else:
                    newcount[s * 2024] += c
            count = newcount
        return str(sum(count.values()))

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
