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
        sum = 0
        for line in data:
            all_nums = [int(n) for n in line]
            if part2:
                pos = 0
                selected = ""
                while len(selected) < 12:
                    s = all_nums[pos:len(all_nums) - 11 + len(selected)]
                    best = max(s)
                    selected += str(best)
                    pos = pos + s.index(best) + 1
                sum += int(selected)
            else:
                best = 0
                for i in range(len(all_nums)):
                    for j in range(i+1, len(all_nums)):
                        selected = int(str(all_nums[i]) + str(all_nums[j]))
                        if selected > best:
                            best = selected
                sum += best
        return str(sum)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
