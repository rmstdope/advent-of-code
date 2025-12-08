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

#     def get_examples(self):
#         examples = []
#         examples.append(Example(input_data='''
#''', answer_a='', answer_b=None))
#         return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        pos = []
        for line in data:
            nums = list(map(int, line.split(',')))
            pos.append((nums[0], nums[1], nums[2]))
        dist = []
        for i1,b1 in enumerate(pos):
            for i2,b2 in enumerate(pos):
                if i1 >= i2:
                    continue
                d = abs(b1[0]-b2[0])*abs(b1[0]-b2[0]) + abs(b1[1]-b2[1])*abs(b1[1]-b2[1]) + abs(b1[2]-b2[2])*abs(b1[2]-b2[2])
                dist.append((d, b1, b2))
        dist.sort(key=lambda x: x[0])
        num = 10
        if len(pos) > 30:
            num = 1000
        if part2:
            num = len(dist)
        cluster = []
        for i in range(num):
            d, b1, b2 = dist[i]
            b1index = -1
            b2index = -1
            for i,c in enumerate(cluster):
                if b1 in c:
                    b1index = i
                if b2 in c:
                    b2index = i
            if b1index != -1 and b2index != -1:
                if b1index != b2index:
                    c1 = cluster[b1index]
                    c2 = cluster[b2index]
                    c1.update(c2)
                    cluster.pop(b2index)
                    
            elif b1index != -1:
                cluster[b1index].add(b2)
            elif b2index != -1:
                cluster[b2index].add(b1)
            else:
                cluster.append(set([b1, b2]))
            cluster.sort(key=lambda x: len(x), reverse=True)
            if part2 and len(cluster[0]) == len(pos):
                return str(b1[0] * b2[0])
        return str(len(cluster[0]) * len(cluster[1])  * len(cluster[2]))

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
