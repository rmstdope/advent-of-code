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
        examples.append(Example(input_data='''1
10
100
2024''', answer_a='37327623', answer_b=None))
        examples.append(Example(input_data='''1
2
3
2024''', answer_a=None, answer_b='23'))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        def new_secret(num):
            def mix(sec, val):
                return sec ^ val
            def prune (sec):
                return sec % 16777216
            num = mix(num, num * 64)
            num = prune(num)
            num = mix(num, num // 32)
            num = prune(num)
            num = mix(num, num * 2048)
            num = prune(num)
            return num
        secrets = []
        for d in data:
            d = int(d)
            # d = 123
            secret = [d % 10]
            for i in range(2000):
                d = new_secret(d)
                secret.append(d % 10)
            secrets.append(secret)
            sum1 += d
        if part2:
            changes = []
            all_changes = set()
            for s in secrets:
                change = dict()
                for i in range(4, len(s)):
                    diffs = (s[i]- s[i - 1], s[i - 1] - s[i - 2], s[i - 2] - s[i - 3], s[i - 3] - s[i - 4])
                    if diffs not in change:
                        all_changes.add(diffs)
                        change[diffs] = s[i]
                changes.append(change)
            maxs = 0
            for i,c in enumerate(all_changes):
                sum1 = 0
                for change in changes:
                    if c in change:
                        sum1 += change[c]
                maxs = max(maxs, sum1)
            return str(maxs)
        else:
            return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
