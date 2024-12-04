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

    def get_examples(self):
        examples = []
        examples.append(Example(input_data='''MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX''', answer_a='18', answer_b='9'))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        def diag(start, dir, word):
            sum = 0
            pos = start
            num = 0
            for i in range(len(word)):
                if pos[0] < 0 or pos[0] >= len(data[0]) or pos[1] < 0 or pos[1] >= len(data):
                    return 0
                if data[pos[0]][pos[1]] != word[num]:
                    return 0
                num += 1
                pos = (pos[0] - dir[0], pos[1] - dir[1])
            return 1
        if part2:
            for y in range(1, len(data) - 1):
                for x in range(1, len(data[0]) - 1):
                    if data[y][x] != 'A':
                        continue
                    ok1 = False
                    if (data[y - 1][x - 1] == 'M' and data[y + 1][x + 1] == 'S') or (data[y - 1][x - 1] == 'S' and data[y + 1][x + 1] == 'M'):
                        if (data[y - 1][x + 1] == 'M' and data[y + 1][x - 1] == 'S') or (data[y - 1][x + 1] == 'S' and data[y + 1][x - 1] == 'M'):
                            sum1 += 1
        else:
            dirs = [(0, 1), (1, 0), (1, 1), (-1, 1)]
            for y in range(len(data)):
                for x in range(len(data[0])):
                    for d in dirs:
                        sum1 += diag((x, y), d, 'XMAS')
                        sum1 += diag((x, y), d, 'SAMX')
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
