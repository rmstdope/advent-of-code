import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().splitlines()
asteroids = []
inview = []
for y,s in enumerate(strs):
    for x,c in enumerate(s):
        if c == '#':
            asteroids.append([x, y])

def is_on_line_segment(point, start, end):
    # Check if the point is collinear with point1 and point2
    if not ((point[1] - start[1]) * (end[0] - start[0]) == (end[1] - start[1]) * (point[0] - start[0])):
        return False  # If not collinear, it can't be on the line segment

    # Check if the point is within the range of x and y coordinates of the line segment
    min_x = min(start[0], end[0])
    max_x = max(start[0], end[0])
    min_y = min(start[1], end[1])
    max_y = max(start[1], end[1])

    return min_x <= point[0] <= max_x and min_y <= point[1] <= max_y

best = 0
besti = -1
for si,aSrc in enumerate(asteroids):
    num = 0
    for di,aDst in enumerate(asteroids):
        if si == di:
            continue
        blocked = False
        for ci,aChk in enumerate(asteroids):
            if si == ci or di == ci:
                continue
            if is_on_line_segment(aChk, aSrc, aDst):
                blocked = True
        if not blocked:
            num += 1
    inview.append(num)
    if num > best:
        best = num
        besti = si

#print(f'{best=}')
#print(f'{asteroids[besti]=}')
part1 = best

# Part 2
# part1 = 0
# station = [11, 13]
station = asteroids[besti]

asteroids.remove(station)
#print(len(asteroids))
blocked = []
nonblocked = []
for aDst in asteroids:
    isBlocked = False
    for aChk in asteroids:
        if aDst == aChk:
            continue
        if is_on_line_segment(aChk, station, aDst):
            isBlocked = True
    if isBlocked:
        blocked.append(aDst)
    else:
        nonblocked.append(aDst)

def remove_in_quad(quad, asteroids, num_removed):
    global part2
    quad_asteroids = []
    comp_v = []
    for a in asteroids:
        if quad == 0 and a[0] >= station[0] and a[1] < station[1]:
            quad_asteroids.append(a)
            comp_v = np.array([0, -1])
        elif quad == 1 and a[0] > station[0] and a[1] >= station[1]:
            quad_asteroids.append(a)
            comp_v = np.array([1, 0])
        elif quad == 2 and a[0] <= station[0] and a[1] > station[1]:
            quad_asteroids.append(a)
            comp_v = np.array([0, 1])
        elif quad == 3 and a[0] < station[0] and a[1] <= station[1]:
            quad_asteroids.append(a)
            comp_v = np.array([-1, 0])
    crossp = []
    crossp_sorted = []
    for a in quad_asteroids:
        v = np.array(a) - np.array(station)
        v = v / np.linalg.norm(v)
        cross = np.cross(comp_v, v).tolist()
        crossp.append(cross)
        crossp_sorted.append(cross)
    crossp_sorted.sort()
    while len(quad_asteroids) > 0:
        v = crossp_sorted.pop(0)
        i = crossp.index(v)
        crossp.pop(i)
        a = quad_asteroids.pop(i)
        num_removed += 1
        if (num_removed == 200):
            part2 = a[0] * 100 + a[1]
    return num_removed     

removed = 0
removed = remove_in_quad(0, nonblocked, removed)
removed = remove_in_quad(1, nonblocked, removed)
removed = remove_in_quad(2, nonblocked, removed)
removed = remove_in_quad(3, nonblocked, removed)

# i = 0
# while i < len(nonblocked):
#     if nonblocked[i][0] >= station[0] or nonblocked[i][1] >= station[1]:
#         del nonblocked[i]
#         removed += 1
#     else:
#         i += 1
# print(f'{removed=}')

# angles = []
# for a in nonblocked:
#     d = np.array(a);
#     s = np.array(station)
#     vec = d - s
#     vec = vec / np.linalg.norm(vec)
#     ref = np.array([-1, 0])
#     angles.append(np.cross(vec, ref))

# sorted_angles = angles
# sorted_angles.sort()
# num200 = angles.index(sorted_angles[200 - removed - 1])
# print(f'{nonblocked[num200]}')
# for y in range(station[1] + 1):
#     for x in range(station[0] + 1):
#         if [x, y] in removed_asteroids:
#             print('#', end='')
#         elif station == [x, y]:
#             print('X', end='')
#         else:
#             print(' ', end='')
#     print('')

print(f'{part1=}, {part2=}')
