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
        raindeers = dict()
        for d in data:
            w = d.split(' ')
            raindeers[w[0]] = (int(w[3]), int(w[6]), int(w[13]))
        time = 2503
        if len(data) != 9:
            time = 1000
        maxlen = 0
        for i,r in enumerate(raindeers.items()):
            cycle_len = r[1][1] + r[1][2]
            cycles = time // cycle_len
            extras = min(r[1][1], time % cycle_len)
            l = cycles * r[1][0] * r[1][1] + extras * r[1][0]
            if l > maxlen:
                maxlen = l
        if part2:
            points = 0
            points = [0 for x in range(len(raindeers))]
            for t in range(1, time + 1):
                lengths = []
                for r in raindeers.items():
                    cycle_len = r[1][1] + r[1][2]
                    cycles = t // cycle_len
                    extras = min(r[1][1], t % cycle_len)
                    l = cycles * r[1][0] * r[1][1] + extras * r[1][0]
                    lengths.append(l)
                max_len = max(lengths)
                for r in range(len(raindeers)):
                    if lengths[r] == max_len:
                        points[r] += 1
            return str(max(points))
        return str(maxlen)

solver = Solver()

solver.solve_part_1()
solver.solve_part_2()
