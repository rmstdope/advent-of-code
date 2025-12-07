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

#     def get_examples(self):
#         examples = []
#         examples.append(Example(input_data='''
#''', answer_a='', answer_b=None))
#         return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        if part2:
            sum1 = 1
            beams = dict()
            for line in data:
                newbeams = dict()
                for i,c in enumerate(line):
                    if c == 'S':
                        beams[i] = 1
                    if c == '^':
                        if  i in beams:
                            sum1 += beams[i]
                            if i-1 not in newbeams:
                                newbeams[i-1] = 0
                            newbeams[i-1] += beams[i]
                            if i-1 in beams:
                                newbeams[i-1] += beams[i-1]
                                del beams[i-1]
                            if i+1 not in newbeams:
                                newbeams[i+1] = 0
                            newbeams[i+1] += beams[i]
                            if i+1 in beams:
                                newbeams[i+1] += beams[i+1]
                                del beams[i+1]
                            del beams[i]
                beams.update(newbeams)           
        else:
            beams = []
            for line in data:
                newbeams = []
                for i,c in enumerate(line):
                    if c == 'S':
                        beams.append(i)
                    if c == '^':
                        if i in beams:
                            sum1 += 1
                            if i-1 not in newbeams:
                                newbeams.append(i-1)
                            if i+1 not in newbeams:
                                newbeams.append(i+1)
                            beams.remove(i)
                beams.extend(newbeams)
                beams = list(set(beams))        
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
