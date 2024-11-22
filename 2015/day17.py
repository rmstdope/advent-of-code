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

    def fill(self, part2, amount, num, fill, containers):
        if amount == fill:
            return (1, num)
        if amount > fill:
            return (0, 10000)
        if len(containers) == 0:
            return (0, 10000)
        sum = self.fill(part2, amount, num, fill, containers[1:])
        ret = self.fill(part2, amount + containers[0], num + 1, fill, containers[1:])
        if not part2:
            return (sum[0] + ret[0], 0)
        if ret[1] < sum[1]:
            return ret
        elif ret[1] == sum[1]:
            return (ret[0] + sum[0], ret[1])
        return sum

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        fill = 150
        if len(data) < 8:
            fill = 25
        sum = 0
        containers = []
        for d in data:
            containers.append(int(d))
        sum = self.fill(part2, 0, 0, fill, containers[1:])
        ret = self.fill(part2, containers[0], 1, fill, containers[1:])
        if not part2:
            return str(sum[0] + ret[0])
        if ret[1] < sum[1]:
            return str(ret[0])
        elif ret[1] == sum[1]:
            return str(ret[0] + sum[0])
        return str(sum[0])

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
