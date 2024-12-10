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

    def get_examples(self):
        examples = []
#         examples.append(Example(input_data='''..90..9
# ...1.98
# ...2..7
# 6543456
# 765.987
# 876....
# 987....''', answer_a='4', answer_b=None))
        examples.append(Example(input_data='''89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732''', answer_a='36', answer_b=None))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        grid = []
        zeros = []
        for d in data:
            row = []
            for c in d:
                if c == '0':
                    zeros.append((len(row), len(grid)))
                row.append(c)
            grid.append(row)
        def find_paths(grid, pos, num):
            x, y = pos
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
                return {('-1', '-1')}
            if grid[y][x] != num:
                return {('-1', '-1')}
            if grid[y][x] == '9':
                # print(f'{num} found at {pos}')
                return {pos}
            newnum = str(int(num) + 1)
            s = set()
            s.update(find_paths(grid, (x + 1, y), newnum))
            s.update(find_paths(grid, (x - 1, y), newnum))
            s.update(find_paths(grid, (x, y + 1), newnum))
            s.update(find_paths(grid, (x, y - 1), newnum))
            return s
        def find_paths2(grid, pos, num):
            x, y = pos
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
                return 0
            if grid[y][x] != num:
                return 0
            if grid[y][x] == '9':
                # print(f'{num} found at {pos}')
                return 1
            newnum = str(int(num) + 1)
            return find_paths2(grid, (x + 1, y), newnum) + find_paths2(grid, (x - 1, y), newnum) + find_paths2(grid, (x, y + 1), newnum) + find_paths2(grid, (x, y - 1), newnum)
        if part2:
            for z in zeros:
                sum1 += find_paths2(grid, z, '0')
        else:
            for z in zeros:
                sum1 += len(find_paths(grid, z, '0')) - 1
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
