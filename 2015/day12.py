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
import json

class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

#    def get_examples(self):
#        examples = []
#         e = Example(input_data='''
# ''', answer_a='', answer_b=None)
#        return examples

    def get_sum(self, part2, data):
        if type(data) is str:
            return 0
        if type(data) is int:
            return data
        if type(data) is list:
            sum = 0
            for d in data:
                sum += self.get_sum(part2, d)
            return sum
        # dictionary
        sum = 0
        for v in data.items():
            if part2 and type(v[1]) is str and v[1] == 'red':
                return 0
            sum += self.get_sum(part2, v[1])
        return sum

    def solve(self, part2, input) -> str:
        data = json.loads(input)
        return str(self.get_sum(part2, data))

solver = Solver()

solver.solve_part_1()
solver.solve_part_2()
