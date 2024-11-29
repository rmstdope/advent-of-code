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
import functools
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
        if part2:
            for d in data:
                d = d.split('-')
                sector = int(d[-1].split('[')[0])
                for w in d:
                    for c in w:
                        if c == '-':
                            continue
                        print(chr((ord(c) - ord('a') + sector) % 26 + ord('a')), end='')
                    print(' ', end='')
                print(sector)
            exit(code=1)
        else:
            sum1 = 0
            def cmp_func(a, b):
                if a[1] == b[1]:
                    return ord(a[0]) - ord(b[0])
                return b[1] - a[1]
            for d in data:
                d = d.split('-')
                sums = ''
                for s in d[:-1]:
                    sums += s
                chksm = d[-1].split('[')[1][:-1]
                com = collections.Counter(sums).most_common(30)
                com.sort(key=functools.cmp_to_key(cmp_func))
                ok = True
                for i in range(5):
                    if com[i][0] != chksm[i]:
                        ok = False
                if ok:
                    sum1 += int(d[-1].split('[')[0])
            return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
