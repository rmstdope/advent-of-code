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
import aoctools
from BaseSolver import BaseSolver
from aocd.models import Example

class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

#     def get_examples(self):
#         examples = []
#         examples.append(Example(input_data='''
#''', answer_a='', answer_b=None))
#         return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        screen = [[0 for row in range(50)] for col in range(6)]
        for d in data:
            d = d.split()
            match (d[0]):
                case 'rect':
                    (xl, yl) = map(int, d[1].split('x'))
                    for y in range(yl):
                        for x in range(xl):
                            screen[y][x] = 1
                case 'rotate':
                    if d[1] == 'row':
                        yr = int(d[2][2:])
                        n = int(d[4])
                        n = n % 50
                        screen[yr] = screen[yr][-n:] + screen[yr][:-n]
                    else:
                        xr = int(d[2][2:])
                        n = int(d[4])
                        n = n % 6
                        save = []
                        for y in range(6):
                            save.append(screen[y][xr])
                        for y in range(6):
                            screen[y][xr] = save[y - n]
        sum1 = 0
        for y in range(6):
            for x in range(50):
                if screen[y][x] == 1:
                    print('*', end='')
                    sum1 += 1
                else:
                    print(' ', end='')
            print()
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
#solver.solve_examples_2()
#solver.solve_problem_2()
