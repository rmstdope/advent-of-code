import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().splitlines()

for y,s in enumerate(strs):
    for x,c in enumerate(s):
        if c == 'S':
            start_x = x
            start_y = y

def modify_map(y, x, c):
    strs[y] = strs[y][:x] + c + strs[y][x + 1:]

#prod
modify_map(start_y, start_x, 'J')

#modify_map(start_y, start_x, 'F')
#modify_map(start_y, start_x, '7')
strs2 = copy.deepcopy(strs)

next_tiles = []
done_tiles = []
next_tiles.append([start_y, start_x, 0])
part1 = 0
while len(next_tiles):
    tile = next_tiles.pop(0)
    x = tile[1]
    y = tile[0]
    c = tile[2]
    if c > part1:
        part1 = c
    done_tiles.append(y * 1000 + x)
    match strs[y][x]:
        case '|':
            if (y - 1) * 1000 + x not in done_tiles:
                next_tiles.append([y - 1, x, c + 1])
            if (y + 1) * 1000 + x not in done_tiles:
                next_tiles.append([y + 1, x, c + 1])
        case '-':
            if y * 1000 + x - 1 not in done_tiles:
                next_tiles.append([y, x - 1, c + 1])
            if y * 1000 + x + 1 not in done_tiles:
                next_tiles.append([y, x + 1, c + 1])
        case 'L':
            if (y - 1) * 1000 + x not in done_tiles:
                next_tiles.append([y - 1, x, c + 1])
            if y * 1000 + x + 1 not in done_tiles:
                next_tiles.append([y, x + 1, c + 1])
        case 'J':
            if (y - 1) * 1000 + x not in done_tiles:
                next_tiles.append([y - 1, x, c + 1])
            if y * 1000 + x - 1 not in done_tiles:
                next_tiles.append([y, x - 1, c + 1])
        case '7':
            if y * 1000 + x - 1 not in done_tiles:
                next_tiles.append([y, x - 1, c + 1])
            if (y + 1) * 1000 + x not in done_tiles:
                next_tiles.append([y + 1, x, c + 1])
        case 'F':
            if y * 1000 + x + 1 not in done_tiles:
                next_tiles.append([y, x + 1, c + 1])
            if (y + 1) * 1000 + x not in done_tiles:
                next_tiles.append([y + 1, x, c + 1])
    modify_map(y, x, '*')

def fill(y, x):
    if x < 0 or x >= len(strs[0]) or y < 0 or y >= len(strs):
        return True
    match strs[y][x]:
        case '#':
            return True
        case '.' | '|' | '-' | 'J' | '7' | 'F' | 'L':
            modify_map(y, x, ' ')
            f = fill(y - 1, x)
            f = f or fill(y + 1, x)
            f = f or fill(y, x - 1)
            f = f or fill(y, x + 1)
            if f:
                modify_map(y, x, '#')
            return f
        case _:
            return False

# for y in range(len(strs)):
#     for x in range(len(strs[y])):
#         to_crawl = []
#         crawled = []
#         escaped = False
#         if strs[y][x] != '*':
#             to_crawl.append(y * 1000 + x)
#             while len(to_crawl):
#                 c = to_crawl.pop()
#                 if c in crawled:
#                     continue
#                 x = c % 1000
#                 y = c // 1000
#                 if x < 0 or x >= len(strs[0]) or y < 0 or y >= len(strs):
#                     escaped = True
#                 else:
#                     if strs[y][x] == '*':
#                         continue
#                     crawled.append(c)
#                     to_crawl.append((y + 1) * 1000 + x)
#                     to_crawl.append((y - 1) * 1000 + x)
#                     to_crawl.append(y * 1000 + x - 1)
#                     to_crawl.append(y * 1000 + x + 1)
#             while len(crawled):
#                 c = crawled.pop()
#                 x = c % 1000
#                 y = c // 1000
#                 if escaped:
#                     modify_map(y, x, '0')
#                 else:
#                     modify_map(y, x, 'I')

part2 = 0

for y in range(len(strs)):
    for x in range(len(strs[y])):
        if strs[y][x] == '*':
            modify_map(y, x, strs2[y][x])
        else:
            modify_map(y, x, '.')

# for s in strs:
#     print(s)

def can_escape(y, x):
    to_crawl = []
    crawled = []
    to_crawl.append(y * 1000 + x)
    while len(to_crawl):
        c = to_crawl.pop()
        if c in crawled:
            continue
        x = c % 1000
        y = c // 1000
        if x < 0 or x >= len(strs[0]) or y < 0 or y >= len(strs):
            return True
        else:
            crawled.append(c)
            # print(y, x)
            if y == 0 or (y > 0 and strs[y - 1][x] not in 'J-7'):
                to_crawl.append((y - 1) * 1000 + x)
            if strs[y][x] not in 'J-7':
                to_crawl.append((y + 1) * 1000 + x)
            if x == 0 or (x > 0 and strs[y][x - 1] not in 'J|L'):
                to_crawl.append(y * 1000 + x - 1)
            if strs[y][x] not in 'J|L':
                to_crawl.append(y * 1000 + x + 1)
    return False

# print(can_escape(6, 19))
# for s in strs:
#     print(s)
for y in range(len(strs)):
    print(y)
    for x in range(len(strs[y])):
        if strs[y][x] == '.' and not can_escape(y, x):
        # if strs[y][x] == 'I':
            part2 += 1

print(f'{part1=}, {part2=}')
