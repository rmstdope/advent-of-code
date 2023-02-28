import numpy as np
import copy

f = open('input.txt')
strs = f.read().splitlines()
part1 = 0
part2 = 0

north = 0
east = 0
facing = 0
for inst in strs:
    c = inst[0]
    num = int(inst[1:])
    if c == 'N':
        north += num
    elif c == 'S':
        north -= num
    elif c == 'E':
        east += num
    elif c == 'W':
        east -= num
    elif c == 'F':
        if facing == 0:
            east += num
        elif facing == 1:
            north -= num
        elif facing == 2:
            east -= num
        else:
            north += num
    elif c == 'R':
        facing = (facing + int(num / 90)) % 4
    elif c == 'L':
        facing = (facing - int(num / 90)) % 4

part1 = abs(north) + abs(east)

north = 0
east = 0
w_north = 1
w_east = 10
for inst in strs:
    c = inst[0]
    num = int(inst[1:])
    if c == 'N':
        w_north += num
    elif c == 'S':
        w_north -= num
    elif c == 'E':
        w_east += num
    elif c == 'W':
        w_east -= num
    elif c == 'F':
        east += num * w_east
        north += num * w_north
    elif c == 'R':
        if int(-num / 90) % 4 == 1:
            temp = w_north
            w_north = w_east
            w_east = -temp
        elif int(-num / 90) % 4 == 2:
            w_east = -w_east
            w_north = -w_north
        elif int(-num / 90) % 4 == 3:
            temp = w_north
            w_north = -w_east
            w_east = temp
    elif c == 'L':
        if int(num / 90) % 4 == 1:
            temp = w_north
            w_north = w_east
            w_east = -temp
        elif int(num / 90) % 4 == 2:
            w_east = -w_east
            w_north = -w_north
        elif int(num / 90) % 4 == 3:
            temp = w_north
            w_north = -w_east
            w_east = temp

part2 = abs(north) + abs(east)

print(f'{part1=}, {part2=}')
