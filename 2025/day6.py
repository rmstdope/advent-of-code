import os
from aocd import data
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
from itertools import groupby


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
        data = input.splitlines()

        if part2:
            values = []
            for c in range(len(data[0]) - 1, -1, -1):
                v = "".join(d[c] for d in data[:-1])
                values.insert(0, v)
            values = [s.strip() for s in values]
            rows = [list(map(int, g)) for k, g in groupby(values, key=bool) if k]
            operands = data[-1].split()
            for i,r in enumerate(rows):
                if operands[i] == "+":
                    sum1 += sum(r)
                else:
                    prod = 1
                    for n in r:
                        prod *= n
                    sum1 += prod
            return str(sum1)
        else:
            nums = []
            for line in data[:-1]:
                nums.append(list(map(int, line.split())))
            operands = data[-1].split()
            for i,o in enumerate(operands):
                col = 0 if o == "+" else 1
                for r in nums:
                    if o == "+":
                        col += r[i]
                    else:
                        col *= r[i]
                sum1 += col
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
