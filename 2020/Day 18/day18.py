import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().splitlines()

class expression:
    def __init__(self, str):
        self.expressions = []
        self.operators = []
        i = 0
        while i < len(str):
            if str[i] == '(':
                par = 1
                substr = ''
                while par > 0:
                    i += 1
                    if str[i] == '(':
                        par += 1
                    elif str[i] == ')':
                        par -= 1
                    if par > 0:
                        substr += str[i]
                self.expressions.append(expression(substr))
            elif str[i] >= '0' and str[i] <= '9':
                numstr = ''
                while i < len(str) and str[i] >= '0' and str[i] <= '9':
                    numstr += str[i]
                    i += 1
                self.expressions.append(int(numstr))
            elif str[i] == '+' or str[i] == '*':
                self.operators.append(str[i])
                i += 1
            else:
                i += 1

    def resolvel2r(self):
        for i,e in enumerate(self.expressions):
            if isinstance(e, expression):
                self.expressions[i] = e.resolvel2r()
        sum = self.expressions[0]
        for i in range(len(self.operators)):
            if self.operators[i] == '+':
                sum += self.expressions[i + 1]
            else:
                sum *= self.expressions[i + 1]
        return sum

    def resolveaddfirst(self):
        for i,e in enumerate(self.expressions):
            if isinstance(e, expression):
                self.expressions[i] = e.resolveaddfirst()
        sum = self.expressions[0]
        newex = [self.expressions[0]]
        newop = []
        for i in range(len(self.operators)):
            if self.operators[i] == '+':
                sum = newex.pop()
                sum += self.expressions[i + 1]
                newex.append(sum)
            else:
                newex.append(self.expressions[i + 1])
                newop.append('*')
        self.operators = newop
        self.expressions = newex
        sum = self.expressions[0]
        for i in range(len(self.operators)):
            sum *= self.expressions[i + 1]
        return sum

part1 = 0
for s in strs:
    e = expression(s)
    part1 += e.resolvel2r()

part2 = 0
for s in strs:
    e = expression(s)
    part2 += e.resolveaddfirst()

print(f'{part1=}, {part2=}')
