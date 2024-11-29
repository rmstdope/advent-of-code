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

#     def get_examples(self):
#         examples = []
#         examples.append(Example(input_data='''
#''', answer_a='', answer_b=None))
#         return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        if part2:
            i = 0
            while i < len(data):
                d1 = list(map(int, data[i + 0].split()))
                d2 = list(map(int, data[i + 1].split()))
                d3 = list(map(int, data[i + 2].split()))
                for j in range(3):
                    if d1[j] + d2[j] > d3[j] and d2[j] + d3[j] > d1[j] and d1[j] + d3[j] > d2[j]:
                        sum1 += 1
                i += 3
        else:
            for d in data:
                d = list(map(int, d.split()))
                if d[0] + d[1] > d[2] and d[1] + d[2] > d[0] and d[0] + d[2] > d[1]:
                    sum1 += 1
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
