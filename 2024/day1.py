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
# ''', answer_a='', answer_b=None))
#         return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        list1 = []
        list2 = []
        for d in data:
            d = d.split()
            list1.append(int(d[0]))
            list2.append(int(d[1]))
        list1.sort()
        list2.sort()
        if part2:
            for i in list1:
                c = list2.count(i)
                sum1 += c * i
            return str(sum1)
        else:
            for i in range(len(list1)):
                sum1 += abs(list1[i] - list2[i])   
            return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
