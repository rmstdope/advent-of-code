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
        code = ''
        if part2:
            forbidden = [(0, 0), (0, 1), (1, 0), (3, 0), (4, 0), (4, 1), (0, 3), (0, 4), (1, 4), (3, 4), (4, 3), (4, 4)]
            translate = ['', '', '1', '', '', '', '2', '3', '4', '', '5', '6', '7', '8', '9', '', 'A', 'B', 'C', '', '', '', 'D', '', '']
            x = 0
            y = 2
            for d in data:
                for c in d:
                    match(c):
                        case 'U':
                            if (x, y - 1) not in forbidden:
                                y = max(0, y - 1)
                        case 'D':
                            if (x, y + 1) not in forbidden:
                                y = min(4, y + 1)
                        case 'L':
                            if (x - 1, y) not in forbidden:
                                x = max(0, x - 1)
                        case 'R':
                            if (x + 1, y) not in forbidden:
                                x = min(4, x + 1)
                code += translate[y * 5 + x]
        else:
            x = 1
            y = 1
            for d in data:
                for c in d:
                    match(c):
                        case 'U':
                            y = max(0, y - 1)
                        case 'D':
                            y = min(2, y + 1)
                        case 'L':
                            x = max(0, x - 1)
                        case 'R':
                            x = min(2, x + 1)
                code += chr(ord('0') + y * 3 + x + 1)
        return code

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
