import os
import numpy as np
import copy
from collections import defaultdict
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

#    def get_examples(self):
#        examples = []
#        examples.append(Example(input_data='''
#''', answer_a='', answer_b=None))
#        return examples

    def fight(self, hp1, dam1, arm1, hp2, dam2, arm2):
        while True:
            hp2 -= max(1, dam1 - arm2)
            if hp2 <= 0:
                return True
            hp1 -= max(1, dam2 - arm1)
            if hp1 <= 0:
                return False

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        hp = int(data[0].split(' ')[2])
        damage = int(data[1].split(' ')[1])
        armor = int(data[2].split(' ')[1])
        weapons = []
        armors = []
        rings = []
        weapons.append((8,4,0))
        weapons.append((10,5,0))
        weapons.append((25,6,0))
        weapons.append((40,7,0))
        weapons.append((74,8,0))
        armors.append((13,0,1))
        armors.append((31,0,2))
        armors.append((53,0,3))
        armors.append((75,0,4))
        armors.append((102,0,5))
        rings.append((25,1,0))
        rings.append((50,2,0))
        rings.append((100,3,0))
        rings.append((20,0,1))
        rings.append((40,0,2))
        rings.append((80,0,3))
        variants = []
        for i in range(len(weapons)):
            for j in range(len(armors) + 1):
                for k in range(len(rings) + 1):
                    for l in range(len(rings) + 1):
                        equipment = []
                        equipment.append(weapons[i])
                        if j < len(armors):
                            equipment.append(armors[j])
                        if k < len(rings):
                            equipment.append(rings[k])
                        if l < len(rings) and l != k:
                            equipment.append(rings[l])
                        if len(equipment) > 0:
                            variants.append([sum(x) for x in zip(*equipment)])
        variants.sort()
        if part2:
            variants.reverse()
            for v in variants:
                if not self.fight(100, v[1], v[2], hp, damage, armor):
                    return str(v[0])
        else:
            for v in variants:
                if self.fight(100, v[1], v[2], hp, damage, armor):
                    return str(v[0])

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
