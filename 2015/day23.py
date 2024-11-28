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

#     def get_examples(self):
#         examples = []
#         examples.append(Example(input_data='''
#''', answer_a='', answer_b=None))
#         return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        instructions = []
        for d in data:
            d = d.split(' ')
            if d[0] == 'jie' or d[0] == 'jio':
                instructions.append((d[0], d[1][:-1], d[2]))
            else:
                instructions.append((d[0], d[1]))
        vars = dict()
        vars['a'] = 0
        vars['b'] = 0
        if part2:
            vars['a'] = 1
        i = 0
        while i >= 0 and i < len(instructions):
            match instructions[i][0]:
                case 'hlf':
                    vars[instructions[i][1]] //= 2
                    i += 1
                case 'tpl':
                    vars[instructions[i][1]] *= 3
                    i += 1
                case 'inc':
                    vars[instructions[i][1]] += 1
                    i += 1
                case 'jmp':
                    i += int(instructions[i][1])
                case 'jie':
                    if vars[instructions[i][1]] % 2 == 0:
                        i += int(instructions[i][2])
                    else:
                        i += 1
                case 'jio':
                    if vars[instructions[i][1]] == 1:
                        i += int(instructions[i][2])
                    else:
                        i += 1
        return str(vars['b'])

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
