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

    def is_abba(self, s):
        for i in range(len(s) - 3):
            if s[i] != s[i + 1] and s[i] == s[i + 3] and s[i + 1] == s[i + 2]:
                return True
        return False

    def get_abas(self, a):
        ret = []
        for s in a:
            for i in range(len(s) - 2):
                if s[i] != s[i + 1] and s[i] == s[i + 2]:
                    ret.append(s[i:i + 3])
        return ret

    def has_bab(self, needles, haystacks):
        for n in needles:
            n = n[1] + n[0] + n[1]
            for h in haystacks:
                if n in h:
                    return True
        return False

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        for d in data:
            s = []
            bs = []
            while len(d) > 0:
                if '[' not in d:
                    s.append(d)
                    d = ''
                else:
                    i1 = d.find('[')
                    i2 = d.find(']')
                    s.append(d[:i1])
                    bs.append(d[i1 + 1:i2])
                    d = d[i2 + 1:]
            ok = False
            if part2:
                abas = self.get_abas(s)
                if self.has_bab(abas, bs):
                    sum1 += 1
            else:
                for x in s:
                    if self.is_abba(x):
                        ok = True
                for x in bs:
                    if self.is_abba(x):
                        ok = False
                if ok:
                    sum1 += 1
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
