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
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############''', answer_a='7036', answer_b='45'))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        grid = []
        shortest = [[], [], [], []]
        for line in data:
            row = []
            rows = []
            for c in line:
                if c == 'S':
                    starty = len(grid)
                    startx = len(row)
                if c == 'E':
                    endy = len(grid)
                    endx = len(row)
                row.append(c)
                rows.append(100000000000)
            grid.append(row)
            shortest[0].append(copy.deepcopy(rows))
            shortest[1].append(copy.deepcopy(rows))
            shortest[2].append(copy.deepcopy(rows))
            shortest[3].append(copy.deepcopy(rows))

        face = 0
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        class BFS2(BFS):
            def __init__(self, start_state):
                BFS.__init__(self, start_state)
                self.best = 100000000000
            
            def visit(self, steps, state):
                if shortest[state[2]][state[1]][state[0]] > steps:
                    shortest[state[2]][state[1]][state[0]] = steps
                if state[0] == endx and state[1] == endy:
                    self.finish(steps)
                    return
                # Move forward
                dir = dirs[state[2]]
                newx = state[0] + dir[0]
                newy = state[1] + dir[1]
                if newx >= 0 and newx < len(grid[0]) and newy >= 0 and newy < len(grid) and grid[newy][newx] != '#':
                    self.add_state(steps + 1, (newx, newy, state[2]))
                # Turn left
                self.add_state(steps + 1000, (state[0], state[1], (state[2] + 1) % 4))
                # Turn right
                self.add_state(steps + 1000, (state[0], state[1], (state[2] - 1) % 4))

        bfs = BFS2((startx, starty, face))
        bfs.run()
        if part2:
            path = set()
            def dfs(x, y, dir, steps):
                for d in range(4):
                    xx = x - dirs[d][0]
                    yy = y - dirs[d][1]
                    if xx < 0 or xx >= len(grid[0]) or yy < 0 or yy >= len(grid) or grid[yy][xx] == '#':
                        continue
                    if (d == dir and shortest[d][yy][xx] == steps - 1):
                        path.add((xx, yy))
                        dfs(xx, yy, d, shortest[d][yy][xx])
                    if (d == (dir + 1) % 4 and shortest[d][yy][xx] == steps - 1001):
                        path.add((xx, yy))
                        dfs(xx, yy, d, shortest[d][yy][xx])
                    if (d == (dir - 1) % 4 and shortest[d][yy][xx] == steps - 1001):
                        path.add((xx, yy))
                        dfs(xx, yy, d, shortest[d][yy][xx])
            dfs(endx, endy, 3, bfs.result)
            l = list(path)
            l.sort()
            return str(len(path) + 1)
        else:
            return str(bfs.result)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
