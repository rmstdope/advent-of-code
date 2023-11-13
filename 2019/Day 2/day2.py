import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
str = f.read().split(',')

def run_intcode(str, s1, s2):
    s = [eval(i) for i in str]
    ip = 0
    s[1] = s1
    s[2] = s2
    op = 0
    while op != 99:
        op = s[ip]
        if (op == 1):
            s[s[ip + 3]] = s[s[ip + 1]] + s[s[ip + 2]]
            ip += 4
        if (op == 2):
            s[s[ip + 3]] = s[s[ip + 1]] * s[s[ip + 2]]
            ip += 4
        if (op == 99):
            ip += 1
    return s

s = run_intcode(str, 12, 2)
part1 = s[0]

for n in range(100):
    for v in range(100):
        s = run_intcode(str, n, v)
        if s[0] == 19690720:
            part2 = n * 100 + v

print(f'{part1=}, {part2=}')
