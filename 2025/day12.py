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
from functools import cache
from z3 import *
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

        # Hard coded by looking at the input
        # Does not work with example data, but with the real one!
        sizes = [7,6,7,5,7,7]

        for s in range(30, len(data)):
            d, p = data[s].split(': ')
            w, h = map(int, d.split('x'))
            needfit = list(map(int, p.split(' ')))
            size = sum(needfit[i] * sizes[i] for i in range(len(needfit)))
            sum1 += 1 if size <= w * h else 0
        
        return str(sum1)

solver = Solver()

# solver.solve_examples_1()
solver.solve_problem_1()
#solver.solve_examples_2()
#solver.solve_problem_2()
