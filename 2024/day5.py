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
import aoctools
from BaseSolver import BaseSolver
from aocd.models import Example

class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

    def get_examples(self):
        examples = []
        examples.append(Example(input_data='''47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47''', answer_a='143', answer_b='123'))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        isrule = True
        rules = []
        ok_rules = []
        nok_rules = []
        for d in data:
            if d == '':
                isrule = False
                continue
            if isrule:
                d = d.split('|')
                rules.append([d[0], d[1]])
            else:
                d = d.split(',')
                ok = True
                for r in rules:
                    if r[0] in d and r[1] in d:
                        if d.index(r[0]) >= d.index(r[1]):
                            ok = False
                if ok:
                    ok_rules.append(d)
                else:
                    nok_rules.append(d)
        for r in ok_rules:
            sum1 += int(r[len(r) // 2])
        if part2:
            new_ok = []
            for n in nok_rules:
                neworder = []
                for c in n:
                    added = False
                    for i in range(len(neworder)):
                        for r in rules:
                            if c == r[0] and neworder[i] == r[1]:
                                neworder.insert(i, c)
                                added = True
                                break
                        if added:
                            break
                    if not added:
                        neworder.append(c)
                new_ok.append(neworder)
            sum1 = 0
            for r in new_ok:
                sum1 += int(r[len(r) // 2])
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
