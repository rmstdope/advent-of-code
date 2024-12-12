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
        examples.append(Example(input_data='''AAAA
BBCD
BBCC
EEEC''', answer_a='140', answer_b='80'))
        examples.append(Example(input_data='''RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE''', answer_a=None, answer_b='1206'))
        return examples

    def solve(self, part2, input) -> str:
        sum1 = 0
        grid = make_grid(input)
        all_visited = set()
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (y, x) not in all_visited:
                    def dfs(y, x, c):
                        if (y, x) in visited:
                            return (0, 0)
                        if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
                            return (0, 1)
                        if grid[y][x] != c:
                            return (0, 1)
                        area.append((y, x))
                        visited.add((y, x))
                        a = 1
                        p = 0
                        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            ny, nx = y + dy, x + dx
                            r = dfs(ny, nx, c)
                            a, p = a + r[0], p + r[1]
                        return (a, p)
                    visited = set()
                    area = []
                    r = dfs(y, x, grid[y][x])
                    all_visited.update(visited)
                    if part2:
                        def num_sides(a):
                            sides = 0
                            fences = set()
                            allplots = set(a)
                            for y, x in a:
                                for yy, xx in [(y + 1, x), (y, x - 1), (y - 1, x), (y, x + 1)]:
                                    if (yy, xx) not in allplots:
                                        fences.add((yy, xx, y, x))
                            for y, x, yy, xx in fences:
                                if (y + 1, x, yy + 1, xx) in fences:
                                    continue
                                if (y, x + 1, yy, xx + 1) in fences:
                                    continue
                                sides += 1
                            return sides                        
                        nums = num_sides(area)
                        # print(f'{y} {x} {r[0]} {nums}')
                        sum1 += r[0] * nums
                    else:
                        sum1 += r[0] * r[1]
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
