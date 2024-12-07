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
        examples.append(Example(input_data='''190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20''', answer_a='3749', answer_b='11387'))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        for i,d in enumerate(data):
            # print(f'{i}')
            d = d.split()
            vals = list(map(int, d[1:]))
            sum = int(d[0][:-1])
            ops = pow(4, len(vals) - 1)
            for x in range(ops):
                t = 3
                s = vals[0]
                p = x
                for v in vals[1:]:
                    if (p & t) == 0:
                        s += v
                    elif (p & t) == 1:
                        s *= v
                    elif (p & t) == 2:
                        if part2:
                            s = int(str(s) + str(v))
                        else:
                            s += v
                    else:
                        s = -1
                        break
                    if s > sum:
                        break
                    p = p // 4
                if sum == s:
                    sum1 += sum
                    break
        return str(sum1)

solver = Solver()

# solver.solve_examples_1()
# solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
