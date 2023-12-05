import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().splitlines()

s = strs[0].split(' ')
seeds = []
for seed in s[1:]:
    seeds.append(int(seed))

maps = []
map = []
for s in strs[2:]:
    if s == '':
        maps.append(map)
    elif s[0] >= 'a' and s[0] <= 'z':
        map = []
    else:
        sp = s.split(' ')
        map.append([int(sp[0]), int(sp[1]), int(sp[2])])
maps.append(map)

part1 = 100000000000
for seed in seeds:
    value = seed
    for map in maps:
        mapped = False
        for m in map:
            if value >= m[1] and value < m[1] + m[2]:
                value += m[0] - m[1]
                break
    if value < part1:
        part1 = value

part2 = 100000000000
s = 0
while s < len(seeds):
    values = []
    values.append([seeds[s], seeds[s] + seeds[s + 1]])
    s += 2
    for map in maps:
        mapped_values = []
        for m in map:
            unmapped_values = []
            for v in values:
                s1 = m[1]
                s2 = m[1] + m[2] - 1
                if v[0] < s1:
                    unmapped_values.append([v[0], min(v[1], s1 - 1)])
                if v[1] > s2:
                    unmapped_values.append([max(v[0], s2 + 1), v[1]])
                if max(v[0], s1) <= min(v[1], s2):
                    mapped_values.append([max(v[0], s1) + m[0] - m[1], min(v[1], s2) + m[0] - m[1]])
            values = unmapped_values
        while len(mapped_values):
            values.append(mapped_values.pop())

    for v in values:
        if v[0] < part2:
            part2 = v[0]
        v = values.pop()

print(f'{part1=}, {part2=}')
