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

    def decompress(self, d, part2):
        i = 0
        sum1 = 0
        while i < len(d):
            if d[i] == '(':
                j = d.find(')', i)
                (a, b) = map(int, d[i + 1:j].split('x'))
                i = j + a + 1
                if part2:
                    a = self.decompress(d[j + 1:j + a + 1], part2)
                sum1 += a * b
                continue
            sum1 += 1
            i += 1
        return sum1

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        for d in data:
            sum1 = self.decompress(d, part2)
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
