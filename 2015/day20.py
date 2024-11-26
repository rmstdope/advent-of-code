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
import aoctools
from BaseSolver import BaseSolver
from aocd.models import Example


class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

#    def get_examples(self):
#        examples = []
#        examples.append(Example(input_data='''
#''', answer_a='', answer_b=None))
#        return examples

    # House n
    # nth elf gives n * 10 presents
    # ...
    # (n/2)th elf (if exists) gives n/2 * 10 presents
    def presents(self, part2, house):
        sum = 0
        divs = aoctools.divisors(house)
        for d in divs:
            if not part2 or d < 50:
                sum += house // d * (11 if part2 else 10)
        return sum

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        house = 1
        while self.presents(part2, house) < int(input):
            house += 1
        return str(house)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
