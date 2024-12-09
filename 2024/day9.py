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
        examples.append(Example(input_data='''2333133121414131402''', answer_a='1928', answer_b='2858'))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        f = []
        id = 0
        isf = True
        files = []
        empties = []
        for c in data[0]:
            if isf:
                files.append((len(f), id, int(c)))
                for i in range(int(c)):
                    f.append(id)
                id += 1
            else:
                if c != '0':
                    empties.append((len(f), int(c)))
                for i in range(int(c)):
                    f.append('.')
            isf = not isf
        if part2:
            fi = len(files) - 1
            while fi > 0:
                ei = 0
                epos, elen = empties[ei]
                fpos, id, flen = files[fi]
                while ei < len(empties) - 1 and flen > elen and fpos > epos:
                    ei += 1
                    epos, elen = empties[ei]
                # if ei == len(empties) - 1:
                #     continue
                if flen <= elen and fpos > epos:
                    files.pop(fi)
                    files.insert(0, (epos, id, flen))
                else:
                    fi -= 1
                    continue
                if elen != flen:
                    empties[ei] = (epos + flen, elen - flen)
                else:
                    empties.pop(ei)
            check = 0
            for pos,id,l in files:
                for i in range(l):
                    check += id * (pos + i)
            return str(check)            
        else:
            end = len(f) - 1
            while f[end] == '.':
                end -= 1
            start = 0
            while start < end:
                if f[start] != '.':
                    start += 1
                elif f[end] == '.':
                    end -= 1
                else:
                    f[start] = f[end]
                    f[end] = '.'
                    start += 1
                    end -= 1
            id = 0
            start = 0
            check = 0
            while f[start] != '.':
                check += f[start] * start
                start += 1
            return str(check)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
