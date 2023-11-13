import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().splitlines()

part1 = 0
for s in strs:
    v = int(s)
    v = int(v / 3)
    v = v - 2
    part1 = part1 + v

part2 = 0
for s in strs:
    v = int(s)
    while v > 0:
        v = int(v / 3)
        v = v - 2
        if v > 0:
            part2 = part2 + v

print(f'{part1=}, {part2=}')
