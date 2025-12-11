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
from functools import cache

class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

    def get_examples(self):
        examples = []
        examples.append(Example(input_data='''aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out''', answer_a='5', answer_b=None))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        graph = {}
        for line in data:
            parts = line.split(': ')
            start = parts[0]
            out = parts[1].split()
            graph[start] = out
        
        @cache
        def num_paths(node, dac, fft):
            if node == 'out':
                if (dac and fft):
                    return 1
                else:
                    return 0
            if node not in graph:
                return 0
            s = 0
            for neighbor in graph[node]:
                new_dac = dac or (neighbor == 'dac')
                new_fft = fft or (neighbor == 'fft')
                s += num_paths(neighbor, new_dac, new_fft)                
            return s
        if part2:            
            sum1 = num_paths('svr', False, False)
        else:
            sum1 = num_paths('you', True, True)
        
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
