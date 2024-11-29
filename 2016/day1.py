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
        data = input.split(', ')
        pos = (0, 0)
        facing = 0
        if part2:
            visited = set()
            for d in data:
                if d[0] == 'R':
                    facing = (facing + 1) % 4
                else:
                    facing = (facing - 1) % 4
                dist = int(d[1:])
                for i in range(dist):
                    if facing == 0:
                        pos = (pos[0], pos[1] + 1)
                    elif facing == 1:
                        pos = (pos[0] + 1, pos[1])
                    elif facing == 2:
                        pos = (pos[0], pos[1] - 1)
                    else:
                        pos = (pos[0] - 1, pos[1])
                    if pos in visited:
                        sum1 = abs(pos[0]) + abs(pos[1])
                        return str(sum1)
                    visited.add(pos)
        else:
            for d in data:
                if d[0] == 'R':
                    facing = (facing + 1) % 4
                else:
                    facing = (facing - 1) % 4
                dist = int(d[1:])
                if facing == 0:
                    pos = (pos[0], pos[1] + dist)
                elif facing == 1:
                    pos = (pos[0] + dist, pos[1])
                elif facing == 2:
                    pos = (pos[0], pos[1] - dist)
                else:
                    pos = (pos[0] - dist, pos[1])
            sum1 = abs(pos[0]) + abs(pos[1])
            return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
