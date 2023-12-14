import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().splitlines()
map = []

def generate_map():
    global map
    map = np.array([[c for c in r] for r in strs])
    # map = [
    #     ['.', '.'],
    #     ['.', 'O'],
    # ]

def tilt_n():
    for x in range(len(map[0])):
        for y in range(len(map)):
            for y2 in range(1, len(map)):
                if map[y2][x] == 'O' and map[y2 - 1][x]=='.':
                    map[y2][x] = '.'
                    map[y2 - 1][x] = 'O'

def tilt_w():
    for y in range(len(map)):
        for x in range(len(map[0])):
            for x2 in range(1, len(map[0])):
                if map[y][x2] == 'O' and map[y][x2 - 1]=='.':
                    map[y][x2] = '.'
                    map[y][x2 - 1] = 'O'

def tilt_s():
    for x in range(len(map[0])):
        for y in range(len(map)):
            for y2 in range(len(map) - 2, -1, -1):
                if map[y2][x] == 'O' and map[y2 + 1][x]=='.':
                    map[y2][x] = '.'
                    map[y2 + 1][x] = 'O'

def tilt_e():
    for y in range(len(map)):
        for x in range(len(map[0])):
            for x2 in range(len(map[0]) - 2, -1, -1):
                if map[y][x2] == 'O' and map[y][x2 + 1]=='.':
                    map[y][x2] = '.'
                    map[y][x2 + 1] = 'O'

def draw():
    for y in range(len(map)):
        for x in range(len(map[0])):
                print(map[y][x], end='')
        print('')

def calc():
    value = 0
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 'O':
                value += len(map) - y
    return value

# for i in range(1):
#     tilt2_n()
#     draw2()
#     print('===================================')
#     tilt2_w()
#     draw2()
#     print('===================================')
#     tilt2_s()
#     draw2()
#     print('===================================')
#     tilt2_e()
#     draw2()
#     print('===================================')

generate_map()
tilt_n()
part1 = calc()

generate_map()
num = 0
cache = {}
data = ()
while data not in cache:
    cache[data] = num
    num += 1
    tilt_n()
    tilt_w()
    tilt_s()
    tilt_e()
    # draw()
    data = ()
    for r in map:
        data += tuple(r)
    if data in cache:
        cycle_len = num - cache[data]
        num_cycles = (1000000000 - num) // cycle_len
        num += num_cycles * cycle_len

for y in range(num, 1000000000):
    tilt_n()
    tilt_w()
    tilt_s()
    tilt_e()

part2 = calc()

print(f'{part1=}, {part2=}')
