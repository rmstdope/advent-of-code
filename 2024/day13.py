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
import z3

class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

    def get_examples(self):
        examples = []
        examples.append(Example(input_data='''Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279''', answer_a='480', answer_b='875318608908'))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        i = 0
        while i < len(data):
            mins = math.inf
            d = data[i].split()
            movea = (int(d[2].split('+')[1][:-1]), int(d[3].split('+')[1]))
            d = data[i + 1].split()
            moveb = (int(d[2].split('+')[1][:-1]), int(d[3].split('+')[1]))
            d = data[i + 2].split()
            price = (int(d[1].split('=')[1][:-1]), int(d[2].split('=')[1]))
            i += 4
            if part2:
                price = (price[0] + 10000000000000, price[1] + 10000000000000)
            s = z3.Solver()
            a, b = z3.Ints('a b')
            for j in range(2):
                s.add(movea[j] * a + moveb[j] * b == price[j])
            if s.check() == z3.sat:
                model = s.model()
                # for d in model.decls():
                #     print ("%s = %s" % (d.name(), model[d]))
                sum1 += 3 * model[a].as_long() + model[b].as_long()
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
