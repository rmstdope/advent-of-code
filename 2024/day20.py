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
        examples.append(Example(input_data='''###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############''', answer_a='44', answer_b=None))
        return examples

    def solve(self, part2, input) -> str:
        sum1 = 0
        grid = []
        for line in input.splitlines():
            row = []
            for c in line:
                if c == 'S':
                    c = '.'
                    startx = len(row)
                    starty = len(grid)
                if c == 'E':
                    c = '.'
                    endx = len(row)
                    endy = len(grid)
                row.append(c)
            grid.append(row)
        class BFS3(BFS2):
            def __init__(self, grid):
                BFS2.__init__(self, grid)
            def visit(self, steps, state):
                x, y = state
                if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
                    return False
                if grid[y][x] == '#':
                    return False
                self.add_state(steps + 1, (x + 1, y))
                self.add_state(steps + 1, (x - 1, y))
                self.add_state(steps + 1, (x, y + 1))
                self.add_state(steps + 1, (x, y - 1))
                return True
        bfs1 = BFS3(grid)
        bfs1.run((startx, starty), (endx, endy))
        bfs2 = BFS3(grid)
        bfs2.run((endx, endy), (startx, starty))
        maxs = bfs1.dist[(endx, endy)]
        maxdist = 2
        if part2:
            maxdist = 20
        for y in range(1, len(grid) - 1):
            # print(y)
            for x in range(1, len(grid[0]) - 1):
                for dx in range(-maxdist, maxdist + 1):
                    for dy in range(-maxdist, maxdist + 1):
                        if dx == 0 and dy == 0:
                            continue
                        dst = abs(dx) + abs(dy)
                        if dst > maxdist:
                            continue
                        num = bfs1.dist[(x, y)] + bfs2.dist[(x + dx, y + dy)] + dst
                        if len(grid) > 50:
                            if maxs - num >= 100:
                                sum1 += 1
                        elif maxs - num > 0:
                            sum1 += 1
        return str(sum1)


solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
