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
        examples.add(Example(input_data='''London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
''', answer_a='605', answer_b='982'))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        distances = dict()
        cities = set()
        for d in data:
            s = d.split(' ')
            distances[s[0] + s[2]] = int(s[4])
            distances[s[2] + s[0]] = int(s[4])
            cities.add(s[0])
            cities.add(s[2])
        mindist = 10000000
        maxdist = 0
        for path in list(itertools.permutations(cities)):
            dist = 0
            for i in range(len(path) - 1):
                dist += distances[path[i] + path[i + 1]]
            if dist < mindist:
                mindist = dist
            if dist > maxdist:
                maxdist = dist
        if part2:
            sum1 = maxdist
        else:
            sum1 = mindist
        return str(sum1)

solver = Solver()

solver.solve_part_1()
solver.solve_part_2()
