import os
import numpy as np
import copy
from collections import defaultdict
import networkx as nx
import sympy
import heapq
import sys
import math
from BaseSolver import BaseSolver

class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        grid = [[0 for col in range(1000)] for row in range(1000)] 
        for d in data:
            inst = d.split(' ')
            if inst[0] == 'toggle':
                c = 0
                x1 = int(inst[1].split(',')[0])
                y1 = int(inst[1].split(',')[1])
                x2 = int(inst[3].split(',')[0])
                y2 = int(inst[3].split(',')[1])
            elif inst[1] == 'on':
                c = 1
                x1 = int(inst[2].split(',')[0])
                y1 = int(inst[2].split(',')[1])
                x2 = int(inst[4].split(',')[0])
                y2 = int(inst[4].split(',')[1])
            else:
                c = 2 
                x1 = int(inst[2].split(',')[0])
                y1 = int(inst[2].split(',')[1])
                x2 = int(inst[4].split(',')[0])
                y2 = int(inst[4].split(',')[1])
            for y in range(y1, y2 + 1):
                for x in range(x1, x2 + 1):
                    if c == 0:
                        if part2:
                            grid[y][x] += 2
                        else:
                            grid[y][x] = 1 - grid[y][x]
                    elif c == 1:
                        if part2:
                            grid[y][x] += 1
                        else:
                            grid[y][x] = 1
                    elif c == 2:
                        if part2:
                            grid[y][x] = max(grid[y][x] - 1, 0)
                        else:
                            grid[y][x] = 0
        for y in range(1000):
            for x in range(1000):
                sum1 += grid[y][x]
        return str(sum1)

solver = Solver()

solver.solve_part_1()
solver.solve_part_2()
