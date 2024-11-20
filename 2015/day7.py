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
from aocd.models import Example

class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

    class Rule:
        def value(self, in1, output):
            self.in1 = in1
            self.output = output
            self.op = 0

        def not_(self, in1, output):
            self.in1 = in1
            self.output = output
            self.op = 1
            
        def and_(self, in1, in2, output):
            self.in1 = in1
            self.in2 = in2
            self.output = output
            self.op = 2

        def or_(self, in1, in2, output):
            self.in1 = in1
            self.in2 = in2
            self.output = output
            self.op = 3

        def rshift(self, in1, in2, output):
            self.in1 = in1
            self.in2 = in2
            self.output = output
            self.op = 4
            
        def lshift(self, in1, in2, output):
            self.in1 = in1
            self.in2 = in2
            self.output = output
            self.op = 5

    def rec(self, wire, rules, resolved) -> int:
        if wire in resolved:
            return resolved[wire]
        if wire.isnumeric():
            return int(wire)
        r = rules[wire]
        match (r.op):
            case 0:
                v = self.rec(r.in1, rules, resolved)
            case 1:
                v = (~self.rec(r.in1, rules, resolved)) & 0xFFFF
            case 2:
                a = self.rec(r.in1, rules, resolved)
                b = self.rec(r.in2, rules, resolved)
                v = a & b
            case 3:
                a = self.rec(r.in1, rules, resolved)
                b = self.rec(r.in2, rules, resolved)
                v = a | b
            case 4:
                v = (self.rec(r.in1, rules, resolved) >> self.rec(r.in2, rules, resolved)) & 0xFFFF
            case 5:
                v = (self.rec(r.in1, rules, resolved) << self.rec(r.in2, rules, resolved)) & 0xFFFF
        resolved[wire] = v
        return v

#     def get_examples(self):
#         e = Example(input_data='''
# ''', answer_a='', answer_b=None)
#         return [e]

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        rules = dict()
        for d in data:
            s = d.split(' ')
            r = self.Rule()
            if len(s) == 3:
                r.value(s[0], s[2])
                rules[s[2]] = r
            elif len(s) == 4:
                r.not_(s[1], s[3])
                rules[s[3]] = r
            else:
                match (s[1]):
                    case 'AND':
                        r.and_(s[0], s[2], s[4])
                    case 'OR':
                        r.or_(s[0], s[2], s[4])
                    case 'RSHIFT':
                        r.rshift(s[0], s[2], s[4])
                    case 'LSHIFT':
                        r.lshift(s[0], s[2], s[4])
                rules[s[4]] = r
        sum1 = self.rec('a', rules, dict())
        if part2:
            rules['b'] = self.Rule()
            rules['b'].value(str(sum1), 'b')
            sum1 = self.rec('a', rules, dict())
        return str(sum1)

solver = Solver()

solver.solve_part_1()
solver.solve_part_2()
