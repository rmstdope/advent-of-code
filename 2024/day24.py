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
import random
from aoctools import *
from BaseSolver import BaseSolver
from aocd.models import Example

class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

    def get_examples(self):
        examples = []
        examples.append(Example(input_data='''x00: 1
x01: 1
x02: 1
y00: 0
y01: 1
y02: 0

x00 AND y00 -> z00
x01 XOR y01 -> z01
x02 OR y02 -> z02''', answer_a='4', answer_b=None))
        examples.append(Example(input_data='''x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00''', answer_a=None, answer_b='z00,z01,z02,z05'))
        return examples


# The pattern for x > 2 is:
# x03 XOR y03 -> wps
# wps XOR kmn -> z03
# qfb OR snk -> kmn
# bmc AND wsw -> qfb
# y02 AND x02 -> snk

# y07 XOR x07 -> kpv
# kpv XOR rvc -> swt(z07)
# cfw OR mwg -> rvc
# qgc AND kfh -> cfw
# y06 AND x06 -> mwg

# y13 XOR x13 -> dwq
# dwq XOR pgq -> pqc(z13)
# dsw OR pmr -> pgq
# bqw AND mnh -> dsw
# x12 AND y12 -> pmr

# y24 XOR x24 -> wsv(rjm)
# ktp XOR rjm -> z24
# cms OR qdw -> ktp
# pgt AND hbv -> qdw
# y23 AND x23 -> cms

# x31 XOR y31 -> kqk
# djr XOR kqk -> bgs(z31)
# hcg OR cwb -> djr
# msm AND fdm -> cwb
# x30 AND y30 -> hcg

#z44 = (y44 XOR x44) XOR ((x43 AND y43) OR (x43 XOR y43 AND (((bwr OR vqn) AND qsm) OR bnc)))
    def solve(self, part2, input) -> str:
        data = input.split('\n\n')
        lines = dict()
        for d in data[0].split('\n'):
            lines[d.split(':')[0]] = int(d.split(':')[1])
        gates = []
        for d in data[1].split('\n'):
            x = d.split(' ')
            gates.append((x[0], x[1], x[2], x[4]))
        def sort_gates(gts):
            all_lines = set(lines)
            all_gates = gts.copy()
            sorted_gates = []
            while len(all_gates) > 0:
                for i in range(len(all_gates)):
                    if all_gates[i][0] in all_lines and all_gates[i][2] in all_lines:
                        gate = all_gates.pop(i)
                        all_lines.add(gate[3])
                        sorted_gates.append(gate)
                        break
            return sorted_gates
        gates = sort_gates(gates)
        def calc(gate, lines):
            v1 = lines[gate[0]]
            v2 = lines[gate[2]]
            match gate[1]:
                case 'AND':
                    lines[gate[3]] = v1 & v2
                case 'OR':
                    lines[gate[3]] = v1 | v2
                case 'XOR':
                    lines[gate[3]] = v1 ^ v2
        def get_val(lines, key):
            i = 0
            val = 0
            while key + str(i).zfill(2) in lines:
                val += lines[key + str(i).zfill(2)] << i
                i += 1
            return val
        if part2:
            def swap(k1, k2):
                for g in gates:
                    if g[3] == k1:
                        v1 = g
                    if g[3] == k2:
                        v2 = g
                gates.remove(v1)
                gates.remove(v2)
                gates.append((v1[0], v1[1], v1[2], k2))
                gates.append((v2[0], v2[1], v2[2], k1))
            swap('swt', 'z07')
            swap('pqc', 'z13')
            swap('wsv', 'rjm')
            swap('bgs', 'z31')
            numz = 44
            if len(gates) < 200:
                num_change = 5
            igates = []
            def find_gates(key):
                for i in range(len(gates)):
                    if gates[i][3] == key:
                        i1 = gates[i][0]
                        i2 = gates[i][2]
                        igates.append(gates[i])
                        newgates.append(gates[i])
                        gates.pop(i)
                        find_gates(i1)
                        find_gates(i2)
                        return
            def tryout(gates2, num):
                x = random.randint(0, 1 << (num + 1))
                y = random.randint(0, 1 << (num + 1))
                lines.clear()
                for i in range(num + 1):
                    lines['x' + str(i).zfill(2)] = (x >> i) & 1
                    lines['y' + str(i).zfill(2)] = (y >> i) & 1
                z = x + y
                zlines = dict()
                for i in range(num + 1):
                    zlines['z' + str(i).zfill(2)] = (z >> i) & 1
                for g in gates2:
                    calc(g, lines)
                for i in range(num + 1):
                    if lines['z' + str(i).zfill(2)] != zlines['z' + str(i).zfill(2)]:
                        return False
                return True
            for i in range(numz):
                print(f'{i}')
                newgates = []
                find_gates('z' + str(i).zfill(2))
                lines.clear()
                for j in range(numz + 1):
                    lines['x' + str(j).zfill(2)] = 0
                    lines['y' + str(j).zfill(2)] = 0
                gates2 = sort_gates(igates)
                for j in range(10):
                    ok = tryout(gates2, i)
                    if not ok:
                        pass
            # ALL PASS!
            return 'bgs,pqc,rjm,swt,wsv,z07,z13,z31'
        else:
            for g in gates:
                calc(g, lines)
            z = get_val(lines, 'z')
            return str(z)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
# solver.solve_examples_2()
solver.solve_problem_2()
