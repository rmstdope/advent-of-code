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
        sum1 = 0
        sum2 = 0
        for d in data:
            dim = d.split('x')
            dim = [int(o) for o in dim]
            dim.sort()
            areas = [dim[0] * dim[1], dim[0] * dim[2], dim[1] * dim[2]]
            smallest_area = min(areas)
            sum1 += areas[0] * 2 + areas[1] * 2 + areas[2] * 2 + smallest_area
            sum2 += dim[0] * 2 + dim[1] * 2 + dim[0] * dim[1] * dim[2]
            
        if part2:
            return str(sum2)
        return str(sum1)

solver = Solver()

solver.solve_part_1()
solver.solve_part_2()
