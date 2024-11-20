import os
import numpy as np
import copy
from collections import defaultdict
import networkx as nx
import sympy
import heapq
import sys
import math
from BaseSolver import BaseSolver

class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        if not part2:
            sum1 = 0
            for d in data:
                vowels = 0
                twice = False
                forbidden = False 
                last_c = '}'
                for i,c in enumerate(d):
                    if c in 'aeiou':
                        vowels += 1
                    if i > 0:
                        if c == last_c:
                            twice = True
                        if c == 'b' and last_c == 'a':
                            forbidden = True 
                        if c == 'd' and last_c == 'c':
                            forbidden = True 
                        if c == 'q' and last_c == 'p':
                            forbidden = True 
                        if c == 'y' and last_c == 'x':
                            forbidden = True 
                    last_c = c
                if twice and not forbidden and vowels >= 3:
                    sum1 += 1
            return str(sum1)
        else:
            sum2 = 0
            for d in data:
                repeat = False
                twice = False
                for i in range(len(d) - 3):
                    if d[i:i + 2] in d[i + 2:]:
                        twice = True
                for i1 in range(28):
                    for i2 in range(28):
                        s = chr(ord('a') + i1)
                        s += chr(ord('a') + i2)
                        s += chr(ord('a') + i1)
                        if s in d:
                            repeat = True
                if repeat and twice:
                    sum2 += 1
            return str(sum2)

solver = Solver()

solver.solve_part_1()
solver.solve_part_2()
