import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().splitlines()
map = []
empty_rows = []
empty_columns = []
for i,s in enumerate(strs):
    if '#' not in s:
        empty_rows.append(i)
for x in range(len(strs[0])):
    empty = True
    for y in range(len(strs)):
        if strs[y][x] == '#':
            empty = False
    if empty:
        empty_columns.append(x)

def get_sum_lengths(p2):
    galaxies = []
    add = 1
    if (p2):
        add = 999999
    real_y = 0
    for y in range(len(strs)):
        if y in empty_rows:
            real_y += add
        real_x = 0
        for x in range(len(strs[0])):
            if x in empty_columns:
                real_x += add
            if strs[y][x] == '#':
                galaxies.append([real_y, real_x])
            real_x +=1
        real_y += 1
    sum = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            sum += abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1])
    return sum

part1 = get_sum_lengths(False)
part2 = get_sum_lengths(True)

print(f'{part1=}, {part2=}')
