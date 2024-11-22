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

    def is_ok(self, part2, comp, val, match):
        if part2:
            if comp == 'cats' or comp == 'trees':
                if val <= match[comp]:
                    return False
            elif comp == 'pomeranians' or comp == 'goldfish':
                if val >= match[comp]:
                    return False
            elif match[comp] != val:
                return False
        else:
            if match[comp] != val:
                return False
        return True
        

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        compound = dict()
        compound['children'] = 3
        compound['cats'] = 7
        compound['samoyeds'] = 2
        compound['pomeranians'] = 3
        compound['akitas'] = 0
        compound['vizslas'] = 0
        compound['goldfish'] = 5
        compound['trees'] = 3
        compound['cars'] = 2
        compound['perfumes'] = 1
        for d in data:
            w = d.split(' ')
            if not self.is_ok(part2, w[2][:-1], int(w[3][:-1]), compound):
                continue
            if not self.is_ok(part2, w[4][:-1], int(w[5][:-1]), compound):
                continue
            if not self.is_ok(part2, w[6][:-1], int(w[7]), compound):
                continue
            return w[1][:-1]
        exit(code=1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
