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

    def issafe(self, d):
        last = -1
        sign = 0
        ok = True
        for i in d:
            if last == -1:
                last = int(i)
                continue
            diff = int(i) - last
            if abs(diff) >= 1 and abs(diff) <= 3:
                if sign != 0:
                    if (diff < 0 and sign < 0) or (diff > 0 and sign > 0):
                        pass
                    else:
                        ok = False
                else:
                    if diff < 0:
                        sign = -1
                    else:
                        sign = 1
            else:
                ok = False
            last = int(i)
        return ok

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        if part2:
            for d in data:
                d = list(map(int, d.split()))
                ok = False
                for i in range(len(d)):
                    dnew = copy.deepcopy(d)
                    dnew.pop(i)
                    if self.issafe(dnew):
                        ok = True
                if ok:
                    sum1 += 1
        else:
            for d in data:
                if self.issafe(list(map(int, d.split()))):
                    sum1 += 1
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
