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
import functools
from aoctools import *
from BaseSolver import BaseSolver
from aocd.models import Example

class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

    def get_examples(self):
        examples = []
        examples.append(Example(input_data='''029A
980A
179A
456A
379A''', answer_a='126384', answer_b=None))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        keys = {'0' : (1, 3),
                'A' : (2, 3),
                '1' : (0, 2),
                '2' : (1, 2),
                '3' : (2, 2),
                '4' : (0, 1),
                '5' : (1, 1),
                '6' : (2, 1),
                '7' : (0, 0),
                '8' : (1, 0),
                '9' : (2, 0)}
        keys2 = {'>' : (2, 1),
                 'v' : (1, 1),
                 '<' : (0, 1),
                 '^' : (1, 0),
                 'A' : (2, 0)}
        def path_ok(pos, dst, p):
            x, y = pos
            for c in p:
                if c == '>':
                    x += 1
                elif c == '<':
                    x -= 1
                elif c == 'v':
                    y += 1
                elif c == '^':
                    y -= 1
                if (0, 3) == (x, y):
                    return False
            return True
        def path_ok2(pos, dst, p):
            x, y = pos
            for c in p:
                if c == '>':
                    x += 1
                elif c == '<':
                    x -= 1
                elif c == 'v':
                    y += 1
                elif c == '^':
                    y -= 1
                if (0, 0) == (x, y):
                    return False
            return True
        for d in data:
            code = int(d[:-1])
            pos = keys['A']
            variants = ['']
            for c in d:
                curr_variants = []
                dst = keys[c]
                delta = (dst[0] - pos[0], dst[1] - pos[1])
                strx = ''
                stry = ''
                if delta[0] > 0:
                    strx = '>' * delta[0]
                elif delta[0] < 0:
                    strx = '<' * -delta[0]
                if delta[1] > 0:
                    stry = 'v' * delta[1]
                elif delta[1] < 0:
                    stry = '^' * -delta[1]
                perms = [strx + stry, stry + strx]
                # perms = [''.join(p) for p in itertools.permutations(strx + stry)]
                no_dups = []
                for p in perms:
                    if p not in no_dups:
                        no_dups.append(p)
                perms = no_dups
                for p in perms:
                    if path_ok(pos, dst, p):
                        curr_variants.append(p + 'A')
                new_variants = []
                for v in variants:
                    for cv in curr_variants:
                        new_variants.append(v + cv)
                variants = new_variants
                pos = dst
            def remote_paths(seq):
                variants = ['']
                pos = keys2['A']
                for c in seq:
                    curr_variants = []
                    dst = keys2[c]
                    delta = (dst[0] - pos[0], dst[1] - pos[1])
                    strx = ''
                    stry = ''
                    if delta[0] > 0:
                        strx = '>' * delta[0]
                    elif delta[0] < 0:
                        strx  = '<' * -delta[0]
                    if delta[1] > 0:
                        stry = 'v' * delta[1]
                    elif delta[1] < 0:
                        stry = '^' * -delta[1]
                    perms = [strx + stry, stry + strx]
                    # perms = [''.join(p) for p in itertools.permutations(strx + stry)]
                    no_dups = []
                    for p in perms:
                        if p not in no_dups:
                            no_dups.append(p)
                    perms = no_dups
                    for p in perms:
                        if path_ok2(pos, dst, p):
                            curr_variants.append(p + 'A')
                    new_variants = []
                    for v in variants:
                        for cv in curr_variants:
                            new_variants.append(v + cv)
                    variants = new_variants
                    pos = dst
                return variants
            num = 2
            if part2:
                num = 25
            @functools.cache
            def shortest(seq, num):
                paths = remote_paths(seq)
                if num == 1:
                    res = min(paths, key=len)
                    return len(res)
                minp = 10**48
                for p in paths:
                    pathl = 0
                    subs = p.split('A')[:-1]
                    for s in subs:
                        pathl += shortest(s + 'A', num - 1)
                    minp = min(minp, pathl)
                return minp
            
            minp = 10**48
            for v in variants:
                subs = v.split('A')[:-1]
                lenp = 0
                for s in subs:
                    lenp += shortest(s + 'A', num)
                minp = min(minp, lenp)
            print(f'{minp} {code}')
            sum1 += minp * code
            
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
