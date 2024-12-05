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

#     def get_examples(self):
#         examples = []
#         examples.append(Example(input_data='''
#''', answer_a='', answer_b=None))
#         return examples

    def solve(self, part2, input) -> str:
        data = split_lines_and_words(input, to_int=True)
        sum1 = 0
        class VM2(VM):
            def __init__(self, program, num_regs):
                VM.__init__(self, program, num_regs, debug_print_every=-1)
                self.regs = [0, 0, 0, 0]
            def execute(self, instr):
                match(instr[0]):
                    case 'cpy':
                        if isinstance(instr[1], int):
                            value = int(instr[1])
                        else:
                            value = self.regs[ord(instr[1][0]) - ord('a')]
                        self.regs[ord(instr[2][0]) - ord('a')] = value
                    case 'inc':
                        self.regs[ord(instr[1][0]) - ord('a')] += 1
                    case 'dec':
                        self.regs[ord(instr[1][0]) - ord('a')] -= 1
                    case 'jnz':
                        if isinstance(instr[1], int):
                            value = int(instr[1])
                        else:
                            value = self.regs[ord(instr[1][0]) - ord('a')]
                        if value != 0:
                            self.jump(instr[2])
        vm = VM2(data, 4)
        if part2:
            vm.regs[2] = 1
        vm.run()
        return str(vm.regs[0])

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
solver.solve_examples_2()
solver.solve_problem_2()
