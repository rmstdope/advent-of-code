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
        examples.append(Example(input_data='''kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn''', answer_a='7', answer_b='co,de,ka,ta'))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        comps = set()
        conns = dict()
        for d in data:
            a, b = d.split('-')
            comps.add(a)
            comps.add(b)
            if a not in conns:
                conns[a] = []
            if b not in conns:
                conns[b] = []
            conns[a].append(b)
            conns[b].append(a)
        if part2:
            longest = set()
            def dfs(c, together, tried):
                for t in together:
                    if c not in conns[t]:
                        return
                together.add(c)
                if len(together) > len(longest):
                    longest.clear()
                    longest.update(together)
                # print(f'{len(together)}')
                for c2 in conns[c]:
                    if c2 not in together and c2 not in tried:
                        tried.add(c2)
                        dfs(c2, together, tried)
                together.remove(c)
            for i,c in enumerate(comps):
                # print(f'{i}')
                dfs(c, set(), set())
            return ','.join(sorted(longest))
        else:
            ok = set()
            for c1 in comps:
                for c2 in conns[c1]:
                    for c3 in conns[c2]:
                        if c1 in conns[c3]:
                            if c1[0] == 't' or c2[0] == 't' or c3[0] == 't':
                                if (c1, c2, c3) not in ok and (c1, c3, c2) not in ok and (c2, c1, c3) not in ok and (c2, c3, c1) not in ok and (c3, c1, c2) not in ok and (c3, c2, c1) not in ok:
                                    ok.add((c1, c2, c3))
                                    sum1 += 1
            return str(sum1)

solver = Solver()

# solver.solve_examples_1()
# solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
