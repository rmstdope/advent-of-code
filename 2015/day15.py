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
        data = input.splitlines()
        while len(data) < 4:
            data.append(f'\nX{len(data)}: capacity 0, durability 0, flavor 0, texture 0, calories 0')
        ingredients = []
        for d in data:
            w = d.split(' ')
            ingredient = (int(w[2][:-1]), int(w[4][:-1]), int(w[6][:-1]), int(w[8][:-1]), int(w[10]))
            ingredients.append(ingredient)
        sum1 = 0
        for i1 in range(0, 101):
            for i2 in range(0, 101 - i1):
                for i3 in range(0, 101 - i1 - i2):
                    i4 = 100 - i1 - i2 - i3
                    capacity = max(0, i1 * ingredients[0][0] + i2 * ingredients[1][0] + i3 * ingredients[2][0] + i4 * ingredients[3][0])
                    durability = max(0, i1 * ingredients[0][1] + i2 * ingredients[1][1] + i3 * ingredients[2][1] + i4 * ingredients[3][1])
                    flavor = max(0, i1 * ingredients[0][2] + i2 * ingredients[1][2] + i3 * ingredients[2][2] + i4 * ingredients[3][2])
                    texture = max(0, i1 * ingredients[0][3] + i2 * ingredients[1][3] + i3 * ingredients[2][3] + i4 * ingredients[3][3])
                    calories = max(0, i1 * ingredients[0][4] + i2 * ingredients[1][4] + i3 * ingredients[2][4] + i4 * ingredients[3][4])
                    if not part2 or calories == 500:
                        sum1 = max(sum1, durability * capacity * flavor * texture)
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
