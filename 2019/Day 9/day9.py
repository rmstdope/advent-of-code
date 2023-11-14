import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
str = f.read().split(',')

class Intcode:
    def __init__(self, str):
        self.s = [eval(i) for i in str]
        self.input = []
        self.ip = 0
        self.base_offset = 0

    def add_input(self, inp):
        self.input.append(inp)

    def get_mode(self, num):
        if num == 0:
            return (self.s[self.ip] // 100) % 10
        elif num == 1:
            return (self.s[self.ip] // 1000) % 10
        return (self.s[self.ip] // 10000) % 10

    def get_parameter(self, num):
        if self.get_mode(num) == 0:
            addr = self.s[self.ip + num + 1]
        elif self.get_mode(num) == 1:
            addr = self.ip + num + 1
        else:
            addr = self.base_offset + self.s[self.ip + num + 1]
        while addr > len(self.s) - 1:
            self.s.append(0)
        return self.s[addr]

    def set_parameter(self, num, val):
        if self.get_mode(num) == 0:
            addr = self.s[self.ip + num + 1]
        elif self.get_mode(num) == 1:
            addr = self.ip + num + 1
        else:
            addr = self.base_offset + self.s[self.ip + num + 1]
        while addr > len(self.s) - 1:
            self.s.append(0)
        self.s[addr] = val

    def run_to_output(self):
        return self.run(True)

    def run_to_finish(self):
        return self.run(False)

    def run(self, run_to_output):
        output = []
        op = 0
        while op != 99:
            op = self.s[self.ip] % 100
            match (op):
                case 1:
                    v1 = self.get_parameter(0)
                    v2 = self.get_parameter(1)
                    self.set_parameter(2, v1 + v2)
                    self.ip += 4
                case 2:
                    v1 = self.get_parameter(0)
                    v2 = self.get_parameter(1)
                    self.set_parameter(2, v1 * v2)
                    self.ip += 4
                case 3:
                    self.set_parameter(0, self.input[0])
                    self.input.pop(0)
                    self.ip += 2
                case 4:
                    output.append(self.get_parameter(0))
                    self.ip += 2
                    if run_to_output:
                        return output
                case 5:
                    if (self.get_parameter(0) != 0):
                        self.ip = self.get_parameter(1)
                    else:
                        self.ip += 3
                case 6:
                    if (self.get_parameter(0) == 0):
                        self.ip = self.get_parameter(1)
                    else:
                        self.ip += 3
                case 7:
                    if self.get_parameter(0) < self.get_parameter(1):
                        self.set_parameter(2, 1)
                    else:
                        self.set_parameter(2, 0)
                    self.ip += 4
                case 8:
                    if self.get_parameter(0) == self.get_parameter(1):
                        self.set_parameter(2, 1)
                    else:
                        self.set_parameter(2, 0)
                    self.ip += 4
                case 9:
                    self.base_offset += self.get_parameter(0)
                    self.ip += 2
                case 99:
                    self.ip += 1
        return output

i = Intcode(str)
i.add_input(1)
part1 = i.run_to_finish()[0]
i = Intcode(str)
i.add_input(2)
part2 = i.run_to_finish()[0]

print(f'{part1=}, {part2=}')
