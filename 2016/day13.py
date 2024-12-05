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
        data = int(data[0])
        sum1 = 0
        class BFS2(BFS):
            def __init__(self, start_state):
                super().__init__(start_state)

            def is_wall(self, x, y):
                if x < 0 or y < 0:
                    return True
                return bin(x*x + 3*x + 2*x*y + y + y*y + data).count('1') % 2 == 1

            def visit(self, steps, pos):
                if (data == 10 and pos == (7, 4)) or (data != 10 and pos == (31, 39)):
                    self.finish(steps)
                    return
                if part2 and steps == 50:
                    return
                for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    new_pos = (pos[0] + d[0], pos[1] + d[1])
                    if self.is_wall(new_pos[0], new_pos[1]):
                        continue
                    self.add_state(steps + 1, new_pos)

        bfs = BFS2((1, 1))
        bfs.run()
        if part2:
            return str(len(bfs.visited))
        else:
            return str(bfs.result)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
