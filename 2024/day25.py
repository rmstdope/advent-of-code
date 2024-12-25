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
        examples.append(Example(input_data='''#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####''', answer_a='3', answer_b=None))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        i = 0
        locks = []
        keys = []
        while i < len(data):
            if data[i] == '#####':
                h = [0, 0, 0, 0, 0]
                for j in range(5):
                    for k in range(7):
                        if data[i + 6 - k][j] == '#':
                            h[j] = 6 - k
                            break
                locks.append(h)
            else:
                h = [0, 0, 0, 0, 0]
                for j in range(5):
                    for k in range(7):
                        if data[i + k][j] == '#':
                            h[j] = 6 - k
                            break
                keys.append(h)
            i += 8
        for l in locks:
            for k in keys:
                ok = True
                for j in range(5):
                    if l[j] + k[j] > 5:
                        ok = False
                if ok:
                    sum1 += 1
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
#solver.solve_examples_2()
#solver.solve_problem_2()
