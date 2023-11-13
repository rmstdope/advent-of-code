import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
str = f.read().splitlines()

part1 = 100000000
part2 = 100000000

def check_collision(x, y, min):
    if abs(x) + abs(y) > min:
        return min
    path = str[1].split(',')
    x2 = 0
    y2 = 0
    for p in path:
        match p[0]:
            case 'R':
                for i in range(int(p[1:])):
                    x2 += 1
                    if x == x2 and y == y2:
                        if abs(x) + abs(y) < min:
                            min = abs(x) + abs(y)
            case 'L':
                for i in range(int(p[1:])):
                    x2 -= 1
                    if x == x2 and y == y2:
                        if abs(x) + abs(y) < min:
                            min = abs(x) + abs(y)
            case 'U':
                for i in range(int(p[1:])):
                    y2 += 1
                    if x == x2 and y == y2:
                        if abs(x) + abs(y) < min:
                            min = abs(x) + abs(y)
            case 'D':
                for i in range(int(p[1:])):
                    y2 -= 1
                    if x == x2 and y == y2:
                        if abs(x) + abs(y) < min:
                            min = abs(x) + abs(y)
    return min

def check_collision2(x, y, steps, min_steps):
    path = str[1].split(',')
    x2 = 0
    y2 = 0
    for p in path:
        if steps > min_steps:
            return min_steps
        match p[0]:
            case 'R':
                for i in range(int(p[1:])):
                    x2 += 1
                    steps += 1
                    if x == x2 and y == y2:
                        if steps < min_steps:
                            min_steps = steps
            case 'L':
                for i in range(int(p[1:])):
                    x2 -= 1
                    steps += 1
                    if x == x2 and y == y2:
                        if steps < min_steps:
                            min_steps = steps
            case 'U':
                for i in range(int(p[1:])):
                    y2 += 1
                    steps += 1
                    if x == x2 and y == y2:
                        if steps < min_steps:
                            min_steps = steps
            case 'D':
                for i in range(int(p[1:])):
                    y2 -= 1
                    steps += 1
                    if x == x2 and y == y2:
                        if steps < min_steps:
                            min_steps = steps
    return min_steps

path = str[0].split(',')
x = 0
y = 0
steps = 0
for p in path:
    match p[0]:
        case 'R':
            print('R')
            for i in range(int(p[1:])):
                x += 1
                steps += 1
                part1 = check_collision(x, y, part1)
                part2 = check_collision2(x, y, steps, part2)
        case 'L':
            print('L')
            for i in range(int(p[1:])):
                x -= 1
                steps += 1
                part1 = check_collision(x, y,  part1)
                part2 = check_collision2(x, y, steps, part2)
        case 'U':
            print('U')
            for i in range(int(p[1:])):
                y += 1
                steps += 1
                part1 = check_collision(x, y, part1)
                part2 = check_collision2(x, y, steps, part2)
        case 'D':
            print('D')
            for i in range(int(p[1:])):
                y -= 1
                steps += 1
                part1 = check_collision(x, y, part1)
                part2 = check_collision2(x, y, steps, part2)


print(f'{part1=}, {part2=}')
