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
        examples.append(Example(input_data='''Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0''', answer_a='4,6,3,5,6,3,5,2,1,0', answer_b=None))
        examples.append(Example(input_data='''Register A: 2024
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0''', answer_a='4,2,5,6,7,7,7,7,3,1,0', answer_b=None))
        examples.append(Example(input_data='''Register A: 10
Register B: 29
Register C: 9

Program: 5,0,5,1,5,4''', answer_a='0,1,2', answer_b=None))
        return examples

    def solve(self, part2, input) -> str:
        data = input.splitlines()
        A = int(data[0].split()[2])        
        B = int(data[1].split()[2])        
        C = int(data[2].split()[2])        
        program = data[4].split()[1]
        class VM2(VM):
            def __init__(self, program):
                super().__init__(program, 3)
                self.regs[0] = A
                self.regs[1] = B
                self.regs[2] = C
                self.output = []

            def getliteral(self, data):
                return data

            def getcombo(self, data):
                match (data):
                    case 0:
                        return 0
                    case 1:
                        return 1
                    case 2:
                        return 2
                    case 3:
                        return 3
                    case 4:
                        return self.regs[0]
                    case 5:
                        return self.regs[1]
                    case 6:
                        return self.regs[2]
                raise NotImplementedError()

            def execute(self, instr):
                self.pc += 1
                op = self.program[self.pc - 2]
                data = self.program[self.pc - 1]
                match (op):
                    case 0:
                        self.regs[0] = self.regs[0] // pow(2, self.getcombo(data))
                    case 1:
                        self.regs[1] = self.regs[1] ^ self.getliteral(data)
                    case 2:
                        self.regs[1] = self.getcombo(data) % 8
                    case 3:
                        if self.regs[0] != 0:
                            self.pc = self.getliteral(data)
                    case 4:
                        self.regs[1] = self.regs[1] ^ self.regs[2]
                    case 5:
                        self.output.append(self.getcombo(data) % 8)
                    case 6:
                        self.regs[1] = self.regs[0] // pow(2, self.getcombo(data))
                    case 7:
                        self.regs[2] = self.regs[0] // pow(2, self.getcombo(data))

        code = [try_int(x) for x in program.split(',')]
        if part2:
            # 2,4,1,7,7,5,1,7,4,6,0,3,5,5,3,0
            # 2,4 - B = A % 8
            # 1,7 - B = B ^ 7
            # 7,5 - C = A / pow(2,B)
            # 1,7 - B = B ^ 7
            # 4,6 - B = B ^ C
            # 0,3 - A = A / 8
            # 5,5 - out(B%8) 
            # 3,0 - jmp 0 if A != 0

            # Insights:
            # out is only dependent on last three bits of A
            # each loop, A is shifted so that the next three bits are in play

            okA = [0]
            for i in range(len(code)):
                newOkA = []
                endcode = code[len(code) - i - 1:]
                for j in range(8):
                    for a in okA:
                        A = (a << 3) + j
                        vm = VM2(code)
                        vm.run()
                        if vm.output == endcode:
                            # print(f'A: {A:>03b}, endcode : {endcode}')
                            newOkA.append(A)
                okA = newOkA
            return min(okA)
        else:
            vm = VM2(code)
            vm.run()
            outp = ''
            for x in vm.output:
                outp += str(x) + ','
            return outp[:-1]

solver = Solver()

solver.solve_examples_1()
solver.solve_problem_1()
#solver.solve_examples_2()
solver.solve_problem_2()
