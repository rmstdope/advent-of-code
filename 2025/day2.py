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

class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

    def get_examples(self):
        examples = []
        examples.append(Example(input_data='''11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124''', answer_a='1227775554', answer_b=None))
        return examples

    def is_valid(self, seq):
        if len(seq) % 2 != 0:
            return True
        half = int(len(seq) / 2)
        for i in range(half):
            if seq[i] != seq[i + half]:
                return True
        return False

    def in_invalid2(self, seq):
        n = len(seq)
        for l in range(1, n // 2 + 1):
            if n % l == 0:
                pattern = seq[:l]
                reps = n // l
                if reps >= 2:
                    if pattern * reps == seq:
                        return True
        return False

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        data = data[0].split(',')
        sum = 0
        for i in range(len(data)):
            d = data[i].split('-')
            for x in range(int(d[0]), int(d[1]) + 1):
                s = str(x)
                if part2:
                    if self.in_invalid2(s):
                        sum += x
                else:
                    if not self.is_valid(s):
                        sum += x

        return str(sum)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
