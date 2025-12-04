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

def ispaper(grid, x, y):
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
        return 0
    if grid[y][x] == '@':
        return 1
    return 0

class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

    def get_examples(self):
        examples = []
        examples.append(Example(input_data='''..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.''', answer_a='13', answer_b='43'))
        return examples



    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        grid = np.array([list(line) for line in data])
        if part2:
            newsum = 1
            while newsum != 0:
                newsum = 0
                for y in range (len(grid)):
                    for x in range(len(grid[0])):
                        if ispaper(grid, x, y) == 1:
                            num = ispaper(grid, x-1, y) + ispaper(grid, x+1, y) + ispaper(grid, x-1, y-1) + ispaper(grid, x, y-1) + ispaper(grid, x+1, y-1) + ispaper(grid, x-1, y+1) + ispaper(grid, x, y+1) + ispaper(grid, x+1, y+1)
                            if num < 4:
                                newsum += 1
                                grid[y][x] = '.'
                sum1 += newsum
        else:
            for y in range (len(grid)):
                for x in range(len(grid[0])):
                    if ispaper(grid, x, y) == 1:
                        num = ispaper(grid, x-1, y) + ispaper(grid, x+1, y) + ispaper(grid, x-1, y-1) + ispaper(grid, x, y-1) + ispaper(grid, x+1, y-1) + ispaper(grid, x-1, y+1) + ispaper(grid, x, y+1) + ispaper(grid, x+1, y+1)
                        if num < 4:
                            sum1 += 1
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
