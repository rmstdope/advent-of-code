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

#    def get_examples(self):
#        examples = []
#         e = Example(input_data='''
# ''', answer_a='', answer_b=None)
#        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        rules = dict()
        names = set()
        for d in data:
            w = d.split(' ')
            rules[w[0] + w[10][:-1]] = int(w[3]) * (1 if w[2] == 'gain' else -1)
            names.add(w[0])
            names.add(w[10][:-1])
        maxhap = 0
        for p in list(itertools.permutations(names)):
            sum = 0
            least = 100000
            for i,n in enumerate(p):
                a = rules[p[i] + p[(i + 1) % len(p)]]
                a += rules[p[(i + 1) % len(p)] + p[i]]
                sum += a
                if a < least:
                    least = a
            if sum > maxhap:
                maxhap = sum
                leastformax = least
        if part2:
            return str(maxhap - leastformax)
        else:
            return str(maxhap)

solver = Solver()

solver.solve_part_1()
solver.solve_part_2()
