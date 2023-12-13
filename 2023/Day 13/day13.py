import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
strs = f.read()

def get_value(map, p2):
    value = 0
    for x in range(len(map[0]) - 1):
        smudges = 0
        for c in range(len(map[0]) // 2):
            x1 = x - c
            x2 = x + c + 1
            if x1 >= 0 and x2 < len(map[0]):
                for y in range(len(map)):
                    if map[y][x1] != map[y][x2]:
                        smudges += 1
        # if smudges > 1:
        #     print('?')
        if (p2 and smudges == 1) or (not p2 and smudges == 0):
            value += x + 1
    for y in range(len(map) - 1):
        smudges = 0
        for c in range(len(map) // 2):
            y1 = y - c
            y2 = y + c + 1
            if y1 >= 0 and y2 < len(map):
                for x in range(len(map[0])):
                    if map[y1][x] != map[y2][x]:
                        smudges += 1
        if (p2 and smudges == 1) or (not p2 and smudges == 0):
            value += 100 * (y + 1)
    return value

part1 = 0
part2 = 0
for map in strs.split('\n\n'):
    part1 += get_value(map.split('\n'), False)
    part2 += get_value(map.split('\n'), True)

print(f'{part1=}, {part2=}')
