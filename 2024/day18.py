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
        examples.append(Example(input_data='''5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0''', answer_a='22', answer_b='6,1'))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        w = 71
        h = 71
        bytes = 1024
        if len(data) < 100:
            w = 7
            h = 7
            bytes = 12
        corr = []
        for d in data:
            d = d.split(',')
            x = int(d[0])
            y = int(d[1])
            corr.append((x, y))
        def create_grid(b):
            g = []
            for y in range(w):
                row = []
                for x in range(h):
                    if (x, y) in corr[:b]:
                        row.append('#')
                    else:
                        row.append('.')
                g.append(row)
            return g
        class BFS2(BFS):
            def __init__(self, startstate):
                super().__init__(startstate)
            def visit(self, steps, state):
                if state[0] == w - 1 and state[1] == h - 1:
                    self.finish(steps)
                for (x, y) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    newx = state[0] + x
                    newy = state[1] + y
                    if newx >= 0 and newx < w and newy >= 0 and newy < h and grid[newy][newx] == '.':
                        self.add_state(steps + 1, (newx, newy))
        if part2:
            numbytes = len(data)
            mintry = 0
            maxtry = len(data)
            while True:
                if mintry == maxtry:
                    break
                newtry = (mintry + maxtry) // 2
                # print('Trying ', newtry)
                grid = create_grid(newtry)
                bfs = BFS2((0, 0))
                bfs.run()
                if bfs.result != None:
                    mintry = newtry + 1
                else:
                    maxtry = newtry
            grid = create_grid(mintry)
            bfs = BFS2((0, 0))
            bfs.run()
            if bfs.result == None:
                mintry = mintry - 1
            return str(corr[mintry][0]) + ',' + str(corr[mintry][1])
        else:
            grid = create_grid(bytes)
            bfs = BFS2((0, 0))
            bfs.run()
            return str(bfs.result)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
