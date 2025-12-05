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

    def add_to_union(self, union, left, right):
        new_union = []
        added = False
        for i, u in enumerate(union):
            if not (right < u[0] or left > u[1]):
                union.pop(i)
                self.add_to_union(union, min(left, u[0]), max(right, u[1]))
                return
        union.append((left, right))

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        ingred = False
        check = []
        fresh = []
        for line in data:
            if line == '':
                ingred = True
            elif ingred:
                check.append(int(line))
            else:
                fresh.append(line)
        union = []
        if part2:
            for f in fresh:
                if '-' in f:
                    parts = f.split('-')
                    left = int(parts[0].strip())
                    right = int(parts[1].strip())
                    self.add_to_union(union, left, right)
                else:
                    add = int(f)
                    self.add_to_union(union, add, add)
            for u in union:
                sum1 += u[1] - u[0] + 1
        else:
            for c in check:
                for f in fresh:
                    if '-' in f:
                        parts = f.split('-')
                        left = int(parts[0].strip())
                        right = int(parts[1].strip())
                        if left <= c <= right:
                            sum1 += 1
                            break
                    else:
                        if int(f.strip()) == c:
                            sum1 += 1
                            break
        
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
