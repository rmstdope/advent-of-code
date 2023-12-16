import numpy as np
import copy
import sys

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().strip().splitlines()

map = [[c for c in row] for row in strs]
map_energy = [[0 for _ in row] for row in strs]

# 1 up, 2, right, 4, down, 8, left
def get_delta(dir):
    match dir:
        case 1:
            return (-1, 0)
        case 2:
            return (0, 1)
        case 4:
            return (1, 0)
        case 8:
            return (0, -1)

# 1 up, 2, right, 4, down, 8, left
def do(dir, p):
    global map_energy
    global map
    #map_energy[y][x] |= dir
    delta = get_delta(dir)
    trace(dir, (p[0] + delta[0], p[1] + delta[1]))

# 1 up, 2, right, 4 down, 8 left
def trace(dir, p):
    global map_energy
    global map
    x = p[1]
    y = p[0]
    if x < 0 or y < 0 or x >= len(map[0]) or y >= len(map):
        return
    if map_energy[y][x] & dir == 0:
        map_energy[y][x] |= dir
        match map[y][x]:
            case '.':
                do(dir, p)
            case '|':
                match dir:
                    case 1 | 4:
                        do(dir, p)
                    case 2 | 8:
                        do(1, p)
                        do(4, p)
            case '-':
                match dir:
                    case 2 | 8:
                        do(dir, p)
                    case 1 | 4:
                        do(2, p)
                        do(8, p)
            case '\\':
                match dir:
                    case 1:
                        do(8, p)
                    case 2:
                        do(4, p)
                    case 4:
                        do(2, p)
                    case 8:
                        do(1, p)
            case '/':
                match dir:
                    case 1:
                        do(2, p)
                    case 2:
                        do(1, p)
                    case 4:
                        do(8, p)
                    case 8:
                        do(4, p)

def get_energy():
    value = 0
    for s in map_energy:
        for d in s:
            if d > 0:
                value += 1
    return value


# 1 up, 2, right, 4, down, 8, left
part1 = 0
sys.setrecursionlimit(100000)
trace(2, (0, 0))
part1 = get_energy()

part2 = 0
for x in range(len(map[0])):
    map_energy = [[0 for _ in row] for row in strs]
    trace(4, (0, x))
    part2 = max(part2, get_energy())
    map_energy = [[0 for _ in row] for row in strs]
    trace(1, (len(map) - 1, x))
    part2 = max(part2, get_energy())

for y in range(len(map)):
    map_energy = [[0 for _ in row] for row in strs]
    trace(2, (y, 0))
    part2 = max(part2, get_energy())
    map_energy = [[0 for _ in row] for row in strs]
    trace(8, (len(map[0]) - 1, y))
    part2 = max(part2, get_energy())


print(f'{part1=}, {part2=}')
