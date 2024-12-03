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

    def get_examples(self):
        examples = []
        examples.append(Example(input_data='''xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
''', answer_a='161', answer_b='48'))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        doit = True
        for d in data:
            sp = d.split('mul(')
            for d in sp:
                if d.find(')') != -1:
                    q = d.split(')')[0]
                    q = q.split(',')
                    if len(q) == 2:
                        if q[0].isdigit() and q[1].isdigit():
                            if not part2 or doit:
                                sum1 += int(q[0]) * int(q[1])
                if part2 and d.find('do()') != -1:
                    doit = True
                    x = d.split('do()')
                    d = x[len(x) - 1]
                if part2 and d.find('don\'t()') != -1:
                    doit = False
        return str(sum1)

solver = Solver()

# solver.solve_examples_1()
# solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
