import os
import numpy as np
import copy
from collections import defaultdict
import networkx as nx
import sympy
import heapq
import sys
import math
import hashlib
from BaseSolver import BaseSolver

class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

    def solve(self, part2, input) -> str:
        num = 1
        while True:
            s = input + str(num)
            hash = hashlib.md5(s.encode())
            hex = hash.hexdigest()
            if hex[0] == '0' and hex[1] == '0' and hex[2] == '0' and hex[3] == '0' and hex[4] == '0' and (not part2 or hex[5] == '0'):
                return str(num)
            num += 1

solver = Solver()

solver.solve_part_1()
solver.solve_part_2()
