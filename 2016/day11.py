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

#     def get_examples(self):
#         examples = []
#         examples.append(Example(input_data='''
#''', answer_a='', answer_b=None))
#         return examples

    # (PrG, PrM, CoG, CoM, CuG, CuM, RuG, RuM, PlG, PlM, E)

    def isok(self, part2, state):
        num = 5
        if part2:
            num = 7
        for i in range(num):
            if state[i * 2 + 1] != state[i * 2]:
                for j in range(num):
                    if i != j and state[i * 2 + 1] == state[j * 2]:
                        return False
        return True

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        sum1 = 0
        state = (0, 0, 1, 2, 1, 2, 1, 2, 1, 2, 0)
        elevator = 10
        if part2:
            state = (0, 0, 1, 2, 1, 2, 1, 2, 1, 2, 0, 0, 0, 0, 0)
            elevator += 4
        end = (3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)
        if part2:
            end = (3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)
        visited = set()
        states = [(0, state)]
        while states:
            steps, state = heapq.heappop(states)
            if state == end:
                sum1 = steps
                break
            indices = [i for i, x in enumerate(state[:-1]) if x == state[elevator]]
            perms = list(itertools.permutations(indices, 2)) + list(itertools.permutations(indices, 1))
            for p in perms:
                if state[elevator] > 0:
                    newstate = list(state)
                    newstate[elevator] = newstate[elevator] - 1
                    for i in p:
                        newstate[i] = newstate[i] - 1
                    newstate = tuple(newstate)
                    if newstate not in visited:
                        visited.add(newstate)
                        if self.isok(part2, newstate):
                            heapq.heappush(states, (steps + 1, newstate))
                        
                if state[elevator] < 3:
                    newstate = list(state)
                    newstate[elevator] = newstate[elevator] + 1
                    for i in p:
                        newstate[i] = newstate[i] + 1
                    newstate = tuple(newstate)
                    if newstate not in visited:
                        visited.add(newstate)
                        if self.isok(part2, newstate):
                            heapq.heappush(states, (steps + 1, newstate))
        return str(sum1)

solver = Solver()

#solver.solve_examples_1()
solver.solve_problem_1()
#solver.solve_examples_2()
solver.solve_problem_2()
