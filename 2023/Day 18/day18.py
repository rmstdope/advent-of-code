import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().strip().splitlines()

# https://en.wikipedia.org/wiki/Shoelace_formula
def shoelace():
    value = 0
    for i in range(len(corners)):
        i2 = (i + 1) % len(corners)    
        value += corners[i][0] * corners[i2][1] - corners[i2][0] * corners[i][1]
    return abs(value) // 2

corners = []
start_x = 0
start_y = 0
end_x = 0
end_y = 0
border = 0
for s in strs:
    start_x = end_x
    start_y = end_y
    d = s.split(' ')
    match d[0]:
        case 'U':
            end_y -= int(d[1])
        case 'D':
            end_y += int(d[1])
        case 'R':
            end_x += int(d[1])
        case 'L':
            end_x -= int(d[1])
    corners.append((start_x, start_y, end_x, end_y))
    border += int(d[1])

part1 = shoelace()
# D and R borders
part1 += border // 2 + 1

corners = []
start_x = 0
start_y = 0
end_x = 0
end_y = 0
border = 0
for s in strs:
    start_x = end_x
    start_y = end_y
    d = s.split(' ')
    dist = int(d[2][2:len(d[2]) - 2], 16)
    match d[2][len(d[2]) - 2]:
        case '3':
            end_y -= dist
        case '1':
            end_y += dist
        case '0':
            end_x += dist
        case '2':
            end_x -= dist
    corners.append((start_x, start_y, end_x, end_y))
    border += dist

part2 = shoelace()
# D and R borders
part2 += border // 2 + 1

print(f'{part1=}, {part2=}')
