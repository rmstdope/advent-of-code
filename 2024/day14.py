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
        examples.append(Example(input_data='''p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3''', answer_a='12', answer_b=None))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        robots = []
        w = 101
        h = 103
        if len(data) <20:
            w = 11
            h = 7
        for d in data:
            d = d.split()
            p = d[0][2:]
            p = p.split(',')
            v = d[1][2:]
            v = v.split(',')
            r = (int(p[0]), int(p[1]), int(v[0]), int(v[1]))
            robots.append(r)
        iter = 100
        if part2:
            iter = 100000000
        for j in range(iter):
            for i in range(len(robots)):
                x, y, vx, vy = robots[i]
                x += vx
                y += vy
                while x < 0:
                    x += w
                while y < 0:
                    y += h
                while x >= w:
                    x -= w
                while y >= h:
                    y -= h
                robots[i] = (x, y, vx, vy)
            if part2:
                c = 0
                for r in robots:
                    for r2 in robots:
                        if r != r2:
                            dx = abs(r[0] - r2[0])
                            dy = abs(r[1] - r2[1])
                            if dx < 2 and dy < 2:
                                c += 1
                if j % 1000 == 0:
                    print(f'Iteration {j} {c}')
                if c > 1000:
                    print(f'Iteration {j} {c}')
                    for y in range(h):
                        for x in range(w):
                            if (x, y) in [(r[0], r[1]) for r in robots]:
                                print('#', end='')
                            else:
                                print('.', end='')
                        print()
        q = [0, 0, 0, 0]
        for r in robots:
            x = r[0] // ((w + 1) // 2)
            y = r[1] // ((h + 1) // 2)
            if r[0] != w // 2 and r[1] != h // 2:
                q[x + 2 * y] += 1
        return str(q[0] * q[1] * q[2] * q[3])

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
