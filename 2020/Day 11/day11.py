import numpy as np
import copy

f = open('input.txt')
strs = f.read().splitlines()
map = []
for i in range(len(strs)):
    map.append([])
    map[i] = []
    map[i][:0] = strs[i]


def occupied(y, x, num):
    dirs = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)]
    c = 0
    for d in range(len(dirs)):
        for n in range(num):
            dy = y + (n + 1) * dirs[d][0]
            dx = x + (n + 1) * dirs[d][1]
            if (dy < 0) or (dy >= len(map)) or (dx < 0) or (dx >= len(map[0])):
                break
            if map[dy][dx] == '#':
                c += 1
                break
            if map[dy][dx] == 'L':
                break
    return c


newmap = map
savedmap = copy.deepcopy(map)

part1 = 0
part2 = 0
for q in range(2):
    same = False
    c = 0
    while not same:
        map = copy.deepcopy(newmap)
        for y in range(len(map)):
            for x in range(len(map[0])):
                if map[y][x] == 'L' and occupied(y, x, 1 if q == 0 else 1000) == 0:
                    newmap[y][x] = '#'
                elif map[y][x] == '#' and occupied(y, x, 1 if q == 0 else 1000) >= (4 if q == 0 else 5):
                    newmap[y][x] = 'L'
        if newmap == map:
            same = True
        c += 1

    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == '#':
                if q == 0:
                    part1 += 1
                else:
                    part2 += 1
    newmap = savedmap

print(f'{part1=}, {part2=}')
