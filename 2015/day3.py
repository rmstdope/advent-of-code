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
        if not part2:
            sum1 = 0
            for d in data:
                visited = set()
                pos = (0, 0)
                visited.add(pos)
                for c in d:
                    if c == '<':
                        pos = (pos[0]-1, pos[1])
                    elif c == '>':
                        pos = (pos[0]+1, pos[1])
                    elif c == '^':
                        pos = (pos[0], pos[1]-1)
                    elif c == 'v':
                        pos = (pos[0], pos[1]+1)
                    if pos not in visited:
                        visited.add(pos)
                sum1 += len(visited)
            return str(sum1)
        else:
            sum2 = 0
            for d in data:
                visited = set()
                pos = [(0, 0), (0, 0)]
                visited.add(pos[0])
                m = 0
                for c in d:
                    if c == '<':
                        pos[m] = (pos[m][0]-1, pos[m][1])
                    elif c == '>':
                        pos[m] = (pos[m][0]+1, pos[m][1])
                    elif c == '^':
                        pos[m] = (pos[m][0], pos[m][1]-1)
                    elif c == 'v':
                        pos[m] = (pos[m][0], pos[m][1]+1)
                    if pos[m] not in visited:
                        visited.add(pos[m])
                    m = 1 - m
                sum2 += len(visited)
            return str(sum2)

solver = Solver()

solver.solve_part_1()
solver.solve_part_2()
