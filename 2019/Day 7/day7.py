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

    def add_input(self, inp):
        self.input.append(inp)

    def get_mode(self, num):
        if num == 0:
            return (self.s[self.ip] // 100) % 10
        elif num == 1:
            return (self.s[self.ip] // 1000) % 10
        return (self.s[self.ip] // 10000) % 10

    def get_parameter(self, num):
        if (self.get_mode(num) == 0):
            return self.s[self.s[self.ip + num + 1]]
        return self.s[self.ip + num + 1]

    def set_parameter(self, num, val):
        if (self.get_mode(num) == 0):
            self.s[self.s[self.ip + num + 1]] = val
        else:
            self.s[self.ip + num + 1] = val

    def run_to_output(self):
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
                    output = self.get_parameter(0)
                    self.ip += 2
                    return output
                case 5:
                    if (self.get_parameter(0 != 0)):
                        self.ip = self.get_parameter(1)
                    else:
                        self.ip += 3
                case 6:
                    if (self.get_parameter(0 == 0)):
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
                case 99:
                    self.ip += 1
        return None

def run_amps(loop):
    best = 0
    add = 0
    if (loop):
        add = 5
    for a in range(add, 5 + add):
        for b in range(add, 5 + add):
            if b == a:
                continue
            for c in range(add, 5 + add):
                if c == a or c == b:
                    continue
                for d in range(add, 5 + add):
                    if d == a or d == b or d == c:
                        continue
                    for e in range(add, 5 + add):
                        if e == a or e == b or e == c or e == d:
                            continue
                        ac = Intcode(str)
                        ac.add_input(a)
                        bc = Intcode(str)
                        bc.add_input(b)
                        cc = Intcode(str)
                        cc.add_input(c)
                        dc = Intcode(str)
                        dc.add_input(d)
                        ec = Intcode(str)
                        ec.add_input(e)
                        p = 0
                        while p == 0 or loop:
                            ac.add_input(p)
                            p = ac.run_to_output()
                            if (p is not None):
                                bc.add_input(p)
                            p = bc.run_to_output()
                            if (p is not None):
                                cc.add_input(p)
                            p = cc.run_to_output()
                            if (p is not None):
                                dc.add_input(p)
                            p = dc.run_to_output()
                            if (p is not None):
                                ec.add_input(p)
                            p = ec.run_to_output()
                            if (p is None):
                                break
                            if p > best:
                                best = p
    return best

part1 = run_amps(False)
part2 = run_amps(True)

print(f'{part1=}, {part2=}')
