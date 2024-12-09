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
        examples.append(Example(input_data='''............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............''', answer_a='14', answer_b='34'))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        map = []
        antennas = []
        for y,d in enumerate(data):
            a = []
            for x, c in enumerate(d):
                a.append(c)
                if c != '.':
                    antennas.append((c, x, y))
            map.append(a)
        locations = set()
        for i1 in range(len(antennas)):
            for i2 in range(i1 + 1, len(antennas)):
                a1 = antennas[i1]
                a2 = antennas[i2]
                if a1[0] != a2[0]:
                    continue
                xdiff = a1[1] - a2[1]
                ydiff = a1[2] - a2[2]
                if a1[1] + xdiff >= 0 and a1[1] + xdiff < len(map[0]) and a1[2] + ydiff >= 0 and a1[2] + ydiff < len(map):
                    locations.add((a1[1] + xdiff, a1[2] + ydiff))
                if a2[1] - xdiff >= 0 and a2[1] - xdiff < len(map[0]) and a2[2] - ydiff >= 0 and a2[2] - ydiff < len(map):
                    locations.add((a2[1] - xdiff, a2[2] - ydiff))
                if abs(xdiff) % 3 == 0 and abs(ydiff) % 3 == 0:
                    locations.add((a1[1] - xdiff // 3, a1[2] - ydiff // 3))
                    locations.add((a2[1] + xdiff // 3, a2[2] + ydiff // 3))
        if part2:
            locations = set()
            for i1 in range(len(antennas)):
                for i2 in range(i1 + 1, len(antennas)):
                    a1 = antennas[i1]
                    a2 = antennas[i2]
                    if a1[0] != a2[0]:
                        continue
                    xdiff = a1[1] - a2[1]
                    ydiff = a1[2] - a2[2]
                    pass
                    for i in range(2, len(map)):
                        while xdiff % i == 0 and ydiff % i == 0:
                            xdiff //= i
                            ydiff //= i
                    mul = 0
                    while a1[1] + xdiff * mul >= 0 and a1[1] + xdiff * mul < len(map[0]) and a1[2] + ydiff * mul >= 0 and a1[2] + ydiff * mul < len(map):
                        locations.add((a1[1] + xdiff * mul, a1[2] + ydiff * mul))
                        mul += 1
                    mul = 0
                    while a2[1] - xdiff * mul >= 0 and a2[1] - xdiff * mul < len(map[0]) and a2[2] - ydiff * mul >= 0 and a2[2] - ydiff * mul < len(map):
                        locations.add((a2[1] - xdiff * mul, a2[2] - ydiff * mul))
                        mul += 1
                    mul = 1
                    while a2[1] + xdiff * mul != a1[1]:
                        locations.add((a2[1] + xdiff * mul, a2[2] + ydiff * mul))
                        mul += 1                
            return str(len(locations))
        else:
            return str(len(locations))

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
