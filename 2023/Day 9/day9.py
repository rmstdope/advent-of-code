import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().splitlines()

def setup(s):
    values = [[]]
    for d in s.split(' '):
        values[0].append(int(d))
    y = 1
    same = False
    while not same:
        values.append([])
        for x in range(len(values[y - 1]) - 1):
            values[y].append(values[y - 1][x + 1] - values[y - 1][x])
        same = True
        for d in range(1, len(values[y])):
            if values[y][d] != 0:
                same = False
        if not same:
            y += 1
    return values

part1 = 0
part2 = 0
for s in strs:
    values = setup(s)
    values[len(values) - 1].append(0)
    for i in reversed(range(len(values) - 1)):
        v1 = values[i][len(values[i]) - 1]
        v2 = values[i + 1][len(values[i + 1]) - 1]
        values[i].append(v1 + v2)
    part1 += values[0][-1]
    values = setup(s)
    values[len(values) - 1].insert(0, 0)
    for i in reversed(range(len(values) - 1)):
        v1 = values[i][0]
        v2 = values[i + 1][0]
        values[i].insert(0, v1 - v2)
    part2 += values[0][0]

print(f'{part1=}, {part2=}')
