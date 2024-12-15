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
#         examples.append(Example(input_data='''#######
# #...#.#
# #.....#
# #..OO@#
# #..O..#
# #.....#
# #######

# <vv<<^^<<^^''', answer_a=None, answer_b='x'))
        examples.append(Example(input_data='''########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<''', answer_a='2028', answer_b=None))
        examples.append(Example(input_data='''##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^''', answer_a='10092', answer_b='9021'))
        return examples

    def move(self, grid, x, y, move):
        startx = x
        starty = y
        while True:
            x += move[0]
            y += move[1]
            if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
                return False
            if grid[y][x] == '#':
                return False
            if grid[y][x] == '.':
                break
            last = grid[y][x]
        while x != startx or y != starty:
            nextx = x - move[0]
            nexty = y - move[1]
            grid[y][x] = grid[nexty][nextx]
            x = nextx
            y = nexty
        return True

    def move2(self, grid, x, y, move):
        last = [(x, y)]
        updown = False
        if move[1] != 0:
            updown = True
        all = []
        while len(last) > 0:
            next = set()
            for xx, yy in last:
                xx += move[0]
                yy += move[1]
                if grid[yy][xx] == '[':
                    next.add((xx, yy))
                    if updown:
                        next.add((xx + 1, yy))                    
                if grid[yy][xx] == ']':
                    next.add((xx, yy))
                    if updown:
                        next.add((xx - 1, yy))
                if grid[yy][xx] == '#':
                    return False
            last = list(next)
            all += list(next)
        all.reverse()
        for xx,yy in all:
            xxp = xx + move[0]
            yyp = yy + move[1]
            grid[yyp][xxp] = grid[yy][xx]
            grid[yy][xx] = '.'
        return True

    def solve(self, part2, inp) -> str:
        data = inp.splitlines()
        sum1 = 0
        grid = []
        i = 0
        while True:
            if len(data[i]) < 2:
                break
            d = data[i]
            row = []
            for c in d:
                if c == '@':
                    c = '.'
                    x = len(row)
                    y = len(grid)
                row.append(c)
            grid.append(row)
            i += 1
        i += 1
        movement = ''
        while i < len(data):
            movement += data[i]
            i += 1
        if part2:
            newgrid = []
            for yy in range(len(grid)):
                row = []
                for xx in range(len(grid[0])):
                    if grid[yy][xx] == '#':
                        row.append('#')
                        row.append('#')
                    if grid[yy][xx] == '.':
                        row.append('.')
                        row.append('.')
                    if grid[yy][xx] == 'O':
                        row.append('[')
                        row.append(']')
                newgrid.append(row)
            grid = newgrid
            x = x * 2
        for m in movement:
            if m == '<':
                move = (-1, 0)
            elif m == '>':
                move = (1, 0)
            elif m == '^':
                move = (0, -1)
            elif m == 'v':
                move = (0, 1)
            # print(f'Move \'{m}\'')
            if part2 and self.move2(grid, x, y, move):
                x += move[0]
                y += move[1]
                # for yy in range(len(grid)):
                #     for xx in range(len(grid[0])):
                #         if xx == x and yy == y:
                #             print('@', end='')
                #         else:
                #             print(grid[yy][xx], end='')
                #     print()
                # ttt = input()
            if not part2 and self.move(grid, x, y, move):
                x += move[0]
                y += move[1]
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == 'O' or grid[y][x] == '[':
                    sum1 += y * 100 + x
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
