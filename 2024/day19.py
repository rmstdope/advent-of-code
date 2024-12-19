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
        examples.append(Example(input_data='''r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb''', answer_a='6', answer_b='16'))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        towels = []
        for d in data[0].split(', '):
            towels.append(d)
        towels = sorted(towels, key=len)
        towels.reverse()
        def num_variants(design):
            ok = collections.Counter()
            ok[0] = 1
            for i in range(len(design)):
                for t in towels:
                    if design[i:i + len(t)] == t:
                        ok[i + len(t)] += ok[i]
            return ok[len(design)]
        for i,d in enumerate(data[2:]):
            # print('towel:', d)
            if part2:
                sum1 += num_variants(d)
            else:
                if num_variants(d):
                    sum1 += 1
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
