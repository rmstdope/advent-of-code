import hashlib
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
        i = 0
        if part2:
            pwd = '        '
            while pwd.find(' ') >= 0:
                hash = hashlib.md5((input + str(i)).encode()).hexdigest()
                if hash.startswith('00000'):
                    pos = int(hash[5], 16)
                    if pos < 8 and pwd[pos] == ' ':
                        pwd = pwd[:pos] + hash[6] + pwd[pos + 1:]
                        print(pwd)
                i += 1
            return pwd
        else:
            pwd = ''
            while len(pwd) < 8:
                hash = hashlib.md5((input + str(i)).encode()).hexdigest()
                if hash.startswith('00000'):
                    pwd = pwd + hash[5]
                i += 1
            return pwd

solver = Solver()

#solver.solve_examples_1()
#solver.solve_problem_1()
#solver.solve_examples_2()
solver.solve_problem_2()
