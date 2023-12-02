import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().splitlines()

part1 = 0
part2 = 0
for str in strs:
    s = str.split(':')
    game = int(s[0].split(' ')[1])
    s2 = s[1].split(';')
    wrong = False
    minred = 0
    minblue = 0
    mingreen = 0
    for set in s2:
        cubestr = set.split(',')
        for cube in cubestr:
            splitstr = cube[1:].split(' ')
            num = int(splitstr[0])
            color = splitstr[1]
            if color == 'red' and num > 12:
                wrong = True
            if color == 'green' and num > 13:
                wrong = True
            if color == 'blue' and num > 14:
                wrong = True
            if color == 'red' and num > minred:
                minred = num
            if color == 'green' and num > mingreen:
                mingreen = num
            if color == 'blue' and num > minblue:
                minblue = num
    if not wrong:
        part1 += game
    part2 += minred * minblue * mingreen

print(f'{part1=}, {part2=}')
