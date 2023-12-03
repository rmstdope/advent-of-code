import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')

strs = f.read().splitlines()

adjacency = dict()
def is_symbol(x, y, num):
    global strs
    global adjacency
    if y < 0:
        return False
    if y >= len(strs):
        return False
    if x < 0:
        return False
    if x >= len(strs[y]):
        return False
    if (strs[y][x] < '0' or strs[y][x] > '9') and strs[y][x] != '.':
        if strs[y][x] == '*':
            index = y * 1000 + x
            if not index in adjacency:
                adjacency[index] = []
            adjacency[index].append(num)
        return True
    return False

part1 = 0
for y, s in enumerate(strs):
    found = False
    fstr = ''
    for x, c in enumerate(s):
        if c >= '0' and c <= '9':
            fstr += c
            if not found:
                found = True
                x1 = x
        elif found:
            adjacent = False
            x2 = x
            num = int(fstr)
            for i in range(x1 - 1, x2 + 1):
                if is_symbol(i, y - 1, num):
                    adjacent = True
                if is_symbol(i, y + 1, num):
                    adjacent = True
            if is_symbol(x1 - 1, y, num):
                adjacent = True
            if is_symbol(x2, y, num):
                adjacent = True
            if adjacent:
                part1 += num
            fstr = ''
            found = False
    if found:
        adjacent = False
        x2 = x
        num = int(fstr)
        for i in range(x1 - 1, x2 + 1):
            if is_symbol(i, y - 1, num):
                adjacent = True
            if is_symbol(i, y + 1, num):
                adjacent = True
        if is_symbol(x1 - 1, y, num):
            adjacent = True
        if is_symbol(x2, y, num):
            adjacent = True
        if adjacent:
            part1 += num
        fstr = ''
        found = False

part2 = 0
for a in adjacency:
    if len(adjacency[a]) == 2:
        part2 += adjacency[a][0] * adjacency[a][1]

print(f'{part1=}, {part2=}')
