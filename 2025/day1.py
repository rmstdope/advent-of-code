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

#     def get_examples(self):
#         examples = []
#         examples.append(Example(input_data='''
#''', answer_a='', answer_b=None))
#         return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        data = [(d[0], int(d[1:])) for d in data]
        number = 50
        password = 0
        if part2:
            for dir, length in data:
                if dir == "R":
                    for _ in range(length):
                        number += 1
                        number %= 100
                        if number == 0:
                            password += 1
                else:
                    for _ in range(length):
                        number -= 1
                        number %= 100
                        if number == 0:
                            password += 1
        else:
            for dir, length in data:
                if dir == "R":
                    number += length
                else:
                    number -= length
                number %= 100
                if number == 0:
                    password += 1
        return str(password)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
