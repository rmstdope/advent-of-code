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
from z3 import *
from aoctools import *
from BaseSolver import BaseSolver
from aocd.models import Example

class Solver(BaseSolver):
    def __init__(self):
        BaseSolver.__init__(self, __file__)

#     def get_examples(self):
#         examples = []
#         examples.append(Example(input_data='''
#''', answer_a='', answer_b=None))
#         return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        target = None
        indicators = None
        for line in data:
            buttons = []
            for l in line.split(' '):
                if l[0] == '[':
                    indicators = l[1:-1]
                elif l[0] == '(':
                    buttons.append(list(map(int, l[1:-1].split(','))))
                else:
                    target = tuple(map(int, l[1:-1].split(',')))
            if part2:
                opt = Optimize()
                button_presses = []
                for i in range(len(buttons)):
                    button_presses.append(Int(f'b{i}'))                

                # All button presses must be non-negative!!
                for bp in button_presses:
                    opt.add(bp >= 0)

                # Button press increments must equal target
                for p, _ in enumerate(target):
                    s = []
                    for i, _ in enumerate(buttons):
                        if p in buttons[i]:
                            s.append(button_presses[i])
                    position_sum = Sum(s)
                    opt.add(position_sum == target[p])                

                # Minimize total button presses
                total_presses = Sum(button_presses)
                opt.minimize(total_presses)

                if opt.check() == sat:
                    model = opt.model()
                    result = 0
                    for bp in button_presses:
                        result += model[bp].as_long()
                    sum1 += result
                else:
                    sum1 += 10e10
            else:
                pq = []
                counter = 0
                start_state = '.'*len(indicators)
                heapq.heappush(pq, (0, counter, start_state))  # cost, tie-breaker, state
                counter += 1
                visited = set()
                visited.add(start_state)
                while pq:
                    cost, _, state = heapq.heappop(pq)
                    if state == indicators:
                        sum1 += cost
                        break
                    for b in buttons:
                        newstate = state
                        for i in b:
                            if state[i] == '.':
                                newstate = newstate[:i] + '#' + newstate[i+1:]
                            else:
                                newstate = newstate[:i] + '.' + newstate[i+1:]
                        if newstate not in visited:
                            visited.add(newstate)
                            heapq.heappush(pq, (cost + 1, counter, newstate))
                            counter += 1
        return str(sum1)

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
