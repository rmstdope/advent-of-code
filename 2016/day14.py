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
        salt = data[0]
        found = False
        data3 = []
        data5 = []
        numhashes = 1
        if part2:
            numhashes = 2017
        def get_d3_d5(salt, i):
            m = md5_hash(salt + str(i))
            for x in range(1, numhashes):
                m = md5_hash(m)
            num = 1
            d5 = []
            d3 = -1
            for j in range(1, len(m)):
                if m[j] == m[j - 1]:
                    num += 1
                else:
                    if num >= 3 and d3 == -1:
                        d3 = m[j - 1]
                    if num >= 5:
                        d5.append(m[j - 1])
                    num = 1
            if num >= 3 and d3 == -1:
                d3 = m[j - 1]
            if num >= 5:
                d5.append(m[j - 1])
            return d3, d5
        for i in range(1001):
            d3, d5 = get_d3_d5(salt, i)
            data3.append(d3)
            if len(d5) > 1:
                raise NotImplementedError()
            data5.append(d5)
        i = -1
        num = 0
        while num < 64:
            i += 1
            if data3[0] != -1:
                for j in range(1, 1001):
                    if data3[0] in data5[j]:
                        num += 1
                        # print(f'Found {num} at {i}')
                        # print(f'->{data3[0]} in {data5[j]}')
                        # m3 = md5_hash(salt + str(i))
                        # m5 = md5_hash(salt + str(i + j))
                        # print(f'->{m3} at {i} and {m5} at {i + j}')
                        break
            d3, d5 = get_d3_d5(salt, i + 1001)
            if len(d5) > 1:
                raise NotImplementedError()
            data3.pop(0)
            data5.pop(0)
            data3.append(d3)
            data5.append(d5)
        return str(i)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
