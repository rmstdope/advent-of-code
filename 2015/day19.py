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
import re
from random import shuffle

def replace_nth(sub, wanted, string, n):
    where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    newString = before + after
    return newString

class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

#    def get_examples(self):
#        examples = []
#        examples.append(Example(input_data='''
#''', answer_a='', answer_b=None))
#        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        rules = []
        for d in data[:-2]:
            w = d.split(' ')
            rules.append((w[0], w[2]))
        molstr = data[len(data) - 1]
        if part2:
            num = sum(1 for c in molstr if c.isupper())
            rn = molstr.count('Rn')
            y = molstr.count('Y')
            return str(num - rn * 2 - 2 * y - 1)
        else:
            molecules = set()
            for r in rules:
                for i in range(molstr.count(r[0])):
                    newstr = replace_nth(r[0], r[1], molstr, i)
                    molecules.add(newstr)
            return str(len(molecules))

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
#solver.solve_examples_2()
solver.solve_problem_2()
