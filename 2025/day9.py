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
        examples.append(Example(input_data='''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3''', answer_a='50', answer_b='24'))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        pairs = []
        for line in data:
            x,y = line.split(',')
            x = int(x)
            y = int(y)
            pairs.append((x,y))
        rects = []
        for i in range(len(pairs) - 1):
            for j in range(i + 1, len(pairs)):
                p1 = pairs[i]
                p2 = pairs[j]
                r = (abs(p1[0]-p2[0])+1)*(abs(p1[1]-p2[1])+1)
                rects.append((r, p1, p2))
        rects.sort(key=lambda x: x[0], reverse=True)
        if part2:
            def is_point_inside(p, pairs):
                px, py = p
                # On edge?
                n = len(pairs)
                for i in range(n):
                    x1, y1 = pairs[i]
                    x2, y2 = pairs[(i + 1) % n]
                    if x1 == x2 == px and min(y1, y2) <= py <= max(y1, y2):
                        return True
                    if y1 == y2 == py and min(x1, x2) <= px <= max(x1, x2):
                        return True
                
                inside = False
                for i in range(len(pairs)):
                    x1, y1 = pairs[i]
                    x2, y2 = pairs[(i + 1) % len(pairs)]
                    if (((y1 >= py) != (y2 >= py)) and
                        (px < (x2 - x1) * (py - y1) / (y2 - y1) + x1)):
                        inside = not inside
                return inside
            
            def is_edge_inside(e, pairs):
                cross = 0
                p1x, p1y = e[0]
                p2x, p2y = e[1]
                for i in range(len(pairs)):
                    px1, py1 = pairs[i]
                    px2, py2 = pairs[(i + 1) % len(pairs)]
                    if p1x == p2x:
                        if px1 != px2:
                            if (min(px1, px2) < p1x < max(px1, px2) and 
                                min(p1y, p2y) < py1 < max(p1y, p2y)):
                                cross += 1
                    else:
                        if py1 != py2:
                            if (min(py1, py2) < p1y < max(py1, py2) and 
                                min(p1x, p2x) < px1 < max(p1x, p2x)):
                                cross += 1
                if cross > 0:
                    return False
                return True
            
            for area, p1, p2 in rects:
                min_x = min(p1[0], p2[0])
                max_x = max(p1[0], p2[0])
                min_y = min(p1[1], p2[1])
                max_y = max(p1[1], p2[1])
                edges = [
                    ((min_x, min_y), (max_x, min_y)),
                    ((min_x, max_y), (max_x, max_y)),
                    ((min_x, min_y), (min_x, max_y)),
                    ((max_x, min_y), (max_x, max_y))
                ]
                corners = [
                    (min_x, min_y),
                    (max_x, min_y),
                    (min_x, max_y),
                    (max_x, max_y)
                ]
                
                all_inside = True
                for e in edges:
                    if not is_edge_inside(e, pairs):
                        all_inside = False
                        break
                
                if all_inside:
                    for c in corners:
                        if not is_point_inside(c, pairs):
                            all_inside = False
                            break
                
                if all_inside:
                    return str(area)            
            return '0'
        else:
            return str(rects[0][0])

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
