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
        data = input.splitlines()[0].split(' ')
        row = int(data[16][:-1])
        col = int(data[18][:-1])
        print(row, col)
        d = 1
        value = 20151125
        x = 1
        y = d
        while True:
            if d != 1:
                value = (value * 252533) % 33554393
            if x == col and y == row:
                return str(value)
            x += 1
            y -= 1
            if y == 0:
                d += 1
                x = 1
                y = d

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
#solver.solve_examples_2()
#solver.solve_problem_2()
