import numpy as np
import copy
import heapq

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().strip().splitlines()

map = [[int(c) for c in s] for s in strs]
#x, y, dir, num, cost
#states = []
#visited = {}

#def run(part2):
#  states.clear()
#  states.append((0, 0, 0, -1, -1))
#  visited.clear()
# states.append((0, 0, 0, 0, 0))
# #states.append((0, 0, 1, 0))

# while len(states) > 0:
#     s = states.pop()
#     visited[(s[0], s[1], s[2], s[3])] = s[4]
#     d1 = (s[2] + 3) % 4
#     d2 = (s[2] + 1) % 4
#     t1 = (s[0], s[1], d1, 0)
#     t11 = (s[0], s[1], d1, 0, s[4])
#     t2 = (s[0], s[1], d2, 0)
#     t22 = (s[0], s[1], d2, 0, s[4])
#     if t1 not in visited:
#         states.append(t11)
#     elif visited[t1] > s[4]:
#             states.append(t11)
#     if t2 not in visited:
#         states.append(t22)
#     elif visited[t2] > s[4]:
#             states.append(t22)
#     if s[3] < 3:
#         x = s[0]
#         y = s[1]
#         match s[2]:
#             case 0:
#                 x += 1
#             case 1:
#                 y += 1
#             case 2:
#                 x -= 1
#             case 3:
#                 y -= 1
#         if x >= 0 and y >= 0 and x < len(map[0]) and y < len(map):
#             fwd1 = (x, y, s[2], s[3] + 1)
#             fwd2 = (x, y, s[2], s[3] + 1, s[4] + map[y][x])
#             if fwd1 not in visited:
#                 states.append(fwd2)
#             elif visited[fwd1] > s[4] + map[y][x]:
#                 states.append(fwd2)


# part1 = 10000000
# for l,v in visited.items():
#      if l[0] == len(map[0]) - 1 and l[1] == len(map) - 1:
#           print(l, v)
#           part1 = min(part1, v)

# part2 = 0


def solve(min_steps, max_steps):
    states = []
    visited = {}
    # cost, x, y, dx, dy, numSteps
    heapq.heappush(states, (0, 0, 0, 0, 1, 0))
    heapq.heappush(states, (0, 0, 0, 1, 0, 0))

    value = 10000000
    while states:
        cost, x, y, old_dx, old_dy, numSteps = heapq.heappop(states)
     
        if x == len(map) - 1 and y == len(map[0]) - 1:
            if numSteps >= min_steps:
                value = min(value, cost)
            continue

        def run(new_dx, new_dy):
            new_x = x + new_dx
            new_y = y + new_dy
            if 0 <= new_x and new_x < len(map) and 0 <= new_y and new_y < len(map[0]):
                new_cost = cost + map[new_x][new_y]
                if new_dx != old_dx or new_dy != old_dy:
                    if numSteps >= min_steps:
                        if (new_x, new_y, new_dx, new_dy, 1) not in visited or new_cost < visited[(new_x, new_y, new_dx, new_dy, 1)]:
                            visited[(new_x, new_y, new_dx, new_dy, 1)] = new_cost
                            heapq.heappush(states, (new_cost, new_x, new_y, new_dx, new_dy, 1))
                else:
                    if numSteps + 1 <= max_steps:
                        if (new_x, new_y, new_dx, new_dy, numSteps + 1) not in visited or new_cost < visited[(new_x, new_y, new_dx, new_dy, numSteps + 1)]:
                            visited[(new_x, new_y, new_dx, new_dy, numSteps + 1)] = new_cost
                            heapq.heappush(states, (new_cost, new_x, new_y, new_dx, new_dy, numSteps + 1))

        if old_dx != -1:
            run(1, 0)
        if old_dx != 1:
            run(-1, 0)
        if old_dy != -1:
            run(0, 1)
        if old_dy != 1:
            run(0, -1)
    return value

part1 = solve(0, 3)
part2 = solve(4, 10)

print(f'{part1=}, {part2=}')
