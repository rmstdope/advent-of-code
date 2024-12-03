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

#     def get_examples(self):
#         examples = []
#         examples.append(Example(input_data='''
#''', answer_a='', answer_b=None))
#         return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        bots = [[] for i in range(210)]
        bot_rule = [None for i in range(210)]
        o0 = None
        o1 = None
        o2 = None
        for d in data:
            d = d.split()
            if d[0] == 'value':
                bots[int(d[5])].append(int(d[1]))
            else:
                rule = (d[5], int(d[6]), d[10], int(d[11]))
                bot_rule[int(d[1])] = rule
        while True:
            for i in range(210):
                if len(bots[i]) == 2:
                    if not part2 and 61 in bots[i] and 17 in bots[i]:
                        return str(i)
                    if bot_rule[i][0] == 'bot':
                        bots[bot_rule[i][1]].append(min(bots[i]))
                    else:
                        if bot_rule[i][1] == 0:
                            o0 = min(bots[i])
                        elif bot_rule[i][1] == 1:
                            o1 = min(bots[i])
                        elif bot_rule[i][1] == 2:
                            o2 = min(bots[i])
                    if bot_rule[i][2] == 'bot':
                        bots[bot_rule[i][3]].append(max(bots[i]))
                    else:
                        if bot_rule[i][3] == 0:
                            o0 = max(bots[i])
                        elif bot_rule[i][3] == 1:
                            o1 = max(bots[i])
                        elif bot_rule[i][3] == 2:
                            o2 = max(bots[i])
                    bots[i] = []
                    break
            if part2 and o0 is not None and o1 is not None and o2 is not None:
                return str(o0 * o1 * o2)

solver = Solver()

#solver.solve_examples_1()
solver.solve_problem_1()
#solver.solve_examples_2()
solver.solve_problem_2()
