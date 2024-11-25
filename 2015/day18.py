import os
import numpy as np
import copy
from collections import defaultdict
import networkx as nx
import sympy
import heapq
import sys
import math
import itertools
from BaseSolver import BaseSolver
from aocd.models import Example

class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

    def get_examples(self):
        examples = []
        examples.append(Example(input_data='''.#.#.#
...##.
#....#
..#...
#.#..#
####..''', answer_a='4', answer_b='17'))
        return examples

    def geton(self, data, y, x):
        if y < 0 or x < 0 or y >= len(data) or x >= len(data[0]):
            return 0
        return 1 if data[y][x] == '#' else 0
        
    def solve(self, part2, input) -> str:
        data = input.splitlines()
        loop = 100
        if len(data) < 100:
            loop = 4 if not part2 else 5            
        if part2:
            newdata = []
            for y in range(len(data)):
                newdata.append([])
                for x in range(len(data[0])):
                    newdata[y].append(data[y][x])
            newdata[0][0] = '#'
            newdata[0][len(data[0]) - 1] = '#'
            newdata[len(data) - 1][0] = '#'
            newdata[len(data) - 1][len(data[0]) - 1] = '#'
            data = newdata
        for i in range(loop):
            newdata = []
            for y in range(len(data)):
                newdata.append([])
                for x in range(len(data[0])):
                    numon = self.geton(data, y - 1, x - 1)
                    numon += self.geton(data, y - 1, x)
                    numon += self.geton(data, y - 1, x + 1)
                    numon += self.geton(data, y, x - 1)
                    numon += self.geton(data, y, x + 1)
                    numon += self.geton(data, y + 1, x - 1)
                    numon += self.geton(data, y + 1, x)
                    numon += self.geton(data, y + 1, x + 1)
                    if data[y][x] == '#':
                        if numon == 2 or numon == 3:
                            newdata[y].append('#')
                        else:
                            newdata[y].append('.')
                    else:
                        if numon == 3:
                            newdata[y].append('#')
                        else:
                            newdata[y].append('.')
            if part2:
                newdata[0][0] = '#'
                newdata[0][len(newdata[0]) - 1] = '#'
                newdata[len(newdata) - 1][0] = '#'
                newdata[len(newdata) - 1][len(newdata[0]) - 1] = '#'
            data = newdata
        sum1 = 0
        for y in range(len(data)):
            for x in range(len(data[0])):
                if data[y][x] == '#':
                    sum1 += 1
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
