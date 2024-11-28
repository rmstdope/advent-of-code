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

    def get_examples(self):
        examples = []
        examples.append(Example(input_data='''Hit Points: 13
Damage: 8
''', answer_a='226', answer_b=None))
        examples.append(Example(input_data='''Hit Points: 14
Damage: 8
''', answer_a='641', answer_b=None))
        return examples

    def in_effect(self, effects, effect):
        for (e, t) in effects:
            if e == effect:
                return True
        return False

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        hp2 = int(data[0].split(' ')[2])
        damage = int(data[1].split(' ')[1])
        states = []
        mana = 500
        hp1 = 50
        turn = 0
        spent = 0
        if hp2 == 13 or hp2 == 14:
            mana = 250
            hp1 = 10
        heapq.heappush(states, (spent, mana, hp1, turn, hp2, damage, [], []))
        while states:
            (spent, mana, hp1, turn, hp2, damage, effects, history) = heapq.heappop(states)
            if (turn % 2 == 0) and part2:
                hp1 -= 1
            if hp1 <= 0:
                continue
            if hp2 <= 0:
                print(history)
                return str(spent)
            armor_add = 0
            new_effects = []
            for i,(e, t) in enumerate(effects):
                if e == 0:
                    armor_add = 7
                if e == 1:
                    hp2 -= 3
                    if hp2 <= 0:
                        print(history)
                        return str(spent)
                if e == 2:
                    mana += 101
                t -= 1
                if t > 0:
                    new_effects.append((e, t))
            effects = new_effects
            if (turn % 2 == 0):
                turn += 1
                # MM
                if mana >= 53:
                    heapq.heappush(states, (spent + 53, mana - 53, hp1, turn, hp2 - 4, damage, effects, history + ['MM']))
                # Drain
                if mana >= 73:
                    heapq.heappush(states, (spent + 73, mana - 73, hp1 + 2, turn, hp2 - 2, damage, effects, history + ['Drain']))
                # Shield
                if mana >= 113 and not self.in_effect(effects, 0):
                    heapq.heappush(states, (spent + 113, mana - 113, hp1, turn, hp2, damage, effects + [(0, 6)], history + ['Shield']))
                # Poison
                if mana >= 173 and not self.in_effect(effects, 1):
                    heapq.heappush(states, (spent + 173, mana - 173, hp1, turn, hp2, damage, effects + [(1, 6)], history + ['Poison']))
                # Recharge
                if mana >= 229 and not self.in_effect(effects, 2):
                    heapq.heappush(states, (spent + 229, mana - 229, hp1, turn, hp2, damage, effects + [(2, 5)], history + ['Recharge']))
            else:
                # Boss damage
                hp1 -= max(1, damage - armor_add) 
                turn += 1
                heapq.heappush(states, (spent, mana, hp1, turn, hp2, damage, effects, history))
        sum1 = 0
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
