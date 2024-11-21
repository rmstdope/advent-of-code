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

    def is_ok(self, pwd):
        ok1 = False
        ok2 = True
        ok3 = 0
        for i in range(len(pwd) - 2):
            if pwd[i] == pwd[i + 1] - 1 and pwd[i + 1] == pwd[i + 2] - 1:
                ok1 = True
        for x in pwd:
            if x == ord('i') - ord('a') or x == ord('o') - ord('a') or x == ord('l') - ord('a'):
                ok2 = False
        i = 0
        while i < len(pwd) - 1:
            if pwd[i] == pwd[i + 1]:
                i += 1
                ok3 += 1
            i += 1
        return ok1 and ok2 and ok3 >= 2

    def solve(self, part2, input) -> str:
        pwd = []
        if part2:
            input = self.solve(False, input,)
        for c in input:
            pwd.append(ord(c) - ord('a'))
        while True:
            carryover = True
            index = 7
            while carryover:
                carryover = False
                pwd[index] = (pwd[index] + 1) % 26
                if pwd[index] == 0:
                    carryover = True
                    index -= 1
            if self.is_ok(pwd):
                break
        answer = ''
        for c in pwd:
            answer += chr(c + ord('a'))
        return answer

solver = Solver()

solver.solve_part_1()
solver.solve_part_2()
