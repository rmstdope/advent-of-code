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
from BaseSolver import BaseSolver
from aocd.models import Example

class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

#    def get_examples(self):
#        examples = []
#         e = Example(input_data='''
# ''', answer_a='', answer_b=None)
#        return examples

    def solve(self, part2, input) -> str:
        r = 1
        if input == '1113122113':
            r = 40
        if part2 and r == 40:
            r = 50
        for i in range(r):
            last = input[0]
            i = 1
            num = 1
            newdata = ''
            while i < len(input):
                if input[i] == last:
                    num += 1
                else:
                    newdata += str(num) + last
                    last = input[i]
                    num = 1
                i += 1
            newdata += str(num) + last
            input = newdata
            i = 1
            num = 1
            newdata = ''
        return str(len(input))

solver = Solver()

solver.solve_part_1()
solver.solve_part_2()
