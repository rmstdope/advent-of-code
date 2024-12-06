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
        examples.append(Example(input_data='''....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
''', answer_a='41', answer_b='6'))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        map = []
        for d in data:
            row = []
            for c in d:
                if c == '^':
                    y = len(map)
                    x = len(row)
                    dir = 0
                    c = '.'
                row.append(c)
            map.append(row)
        visited = set()
        pos = (x, y, dir)
        if part2:
            for oy in range(len(map)):
                for ox in range(len(map[0])):
                    savemap = copy.deepcopy(map)
                    savepos = pos
                    x,y,dir = pos
                    if ox == x and oy == y:
                        continue
                    if map[oy][ox] != '#':
                        map[oy][ox] = '#'
                    visited = set()
                    ok = True
                    while pos not in visited:
                        visited.add(pos)
                        if dir == 0:
                            if y > 0 and map[y - 1][x] == '#':
                                dir = 1
                            else:
                                y -= 1
                        elif dir == 1:
                            if x < len(map[0]) - 1 and map[y][x + 1] == '#':
                                dir = 2
                            else:
                                x += 1
                        elif dir == 2:
                            if y < len(map) - 1 and map[y + 1][x] == '#':
                                dir = 3
                            else:
                                y += 1
                        elif dir == 3:
                            if x > 0 and map[y][x - 1] == '#':
                                dir = 0
                            else:
                                x -= 1
                        if y < 0 or y >= len(map) or x < 0 or x >= len(map[0]):
                            ok = False
                            break
                        map[y][x] = 'X'
                        pos = (x, y, dir)
                    map = copy.deepcopy(savemap)
                    pos = savepos
                    if ok:
                        sum1 += 1
            return str(sum1)
        else:
            while pos not in visited:
                visited.add(pos)
                if dir == 0:
                    if y > 0 and map[y - 1][x] == '#':
                        dir = 1
                    else:
                        y -= 1
                elif dir == 1:
                    if x < len(map[0]) - 1 and map[y][x + 1] == '#':
                        dir = 2
                    else:
                        x += 1
                elif dir == 2:
                    if y < len(map) - 1 and map[y + 1][x] == '#':
                        dir = 3
                    else:
                        y += 1
                elif dir == 3:
                    if x > 0 and map[y][x - 1] == '#':
                        dir = 0
                    else:
                        x -= 1
                if y < 0 or y >= len(map) or x < 0 or x >= len(map[0]):
                    break
                map[y][x] = 'X'
                pos = (x, y, dir)
            for row in map:
                for c in row:
                    if c == 'X':
                        sum1 += 1
            return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
