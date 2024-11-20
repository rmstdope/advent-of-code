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
        #f = open('prod.txt')
        #input = f.read().strip()
        p1 = 0
        for i,c in enumerate(input):
            if c == '(':
                p1 += 1
            else:
                p1 -= 1
                if part2 and p1 < 0:
                    return str(i + 1)
        return str(p1)

solver = Solver()

solver.solve_part_1()
solver.solve_part_2()
