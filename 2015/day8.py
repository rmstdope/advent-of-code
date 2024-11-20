import os
import numpy as np
import copy
from collections import defaultdict
import networkx as nx
import sympy
import heapq
import sys
import math
from BaseSolver import BaseSolver

class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

#     def get_examples(self):
#         e = Example(input_data='''
# ''', answer_a='', answer_b=None)
#         return [e]

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        for d in data:
            d = d.strip()
            d_save = d
            code_len = len(d)
            mem_len = len(d)
            mem_len -= 2
            while '\\\\' in d:
                d = d.replace('\\\\', 'q', 1)
                mem_len -= 1
            while '\\"' in d:
                d = d.replace('\\"', 'q', 1)
                mem_len -= 1
            while '\\x' in d:
                d = d.replace('\\x', 'q', 1)
                mem_len -= 3
            if part2:
                mem_len = code_len
                code_len = len(d_save)
                code_len += 2
                code_len += d_save.count('\\')
                code_len += d_save.count('"')
            sum1 += code_len - mem_len 
        return str(sum1)

solver = Solver()

solver.solve_part_1()
solver.solve_part_2()
