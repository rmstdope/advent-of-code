import numpy as np
import copy
import math

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().splitlines()

def get_start_state():
    global strs
    pos = []
    vel = []
    for s in strs:
        coords = s.split('=')
        pos.append([int(coords[1].split(',')[0]),  
                        int(coords[2].split(',')[0]),  
                        int(coords[3].split('>')[0])])
        vel.append([0, 0, 0])
    return pos,vel

def update_velocity(pos, vel):
    for i in range(3):
        update_velocity_comp(pos, vel, i)

def update_velocity_comp(pos, vel, i):
    for a in range(len(pos)):
        for b in range(a + 1, len(pos)):
            if pos[a][i] < pos[b][i]:
                vel[a][i] += 1
                vel[b][i] -= 1
            elif pos[a][i] > pos[b][i]:
                vel[a][i] -= 1
                vel[b][i] += 1

def update_position(pos, vel):
    for i in range(3):
        update_position_comp(pos, vel, i)

def update_position_comp(pos, vel, i):
    for a in range(len(pos)):
        pos[a][i] += vel[a][i]

def get_energy(pos, vel):
    total = 0
    for a in range(len(pos)):
        pot_energy = 0
        kin_energy = 0
        for i in range(3):
            pot_energy += abs(pos[a][i])
            kin_energy += abs(vel[a][i])
        total += pot_energy * kin_energy
    return total

def get_cycle(pos, vel, i):
    target = []
    num = 0
    for a in range(len(pos)):
        target.append(pos[a][i])
    while True:
        num += 1
        update_velocity_comp(pos, vel, i)
        update_position_comp(pos, vel, i)
        ok = True
        for a in range(len(pos)):
            if pos[a][i] != target[a] or vel[a][i] != 0:
                ok = False
        if ok:
            return num

pos,vel = get_start_state()
for i in range(1000):
    update_velocity(pos, vel)
    update_position(pos, vel)
part1 = get_energy(pos, vel)

pos,vel = get_start_state()
x = get_cycle(pos, vel, 0)
y = get_cycle(pos, vel, 1)
z = get_cycle(pos, vel, 2)

def find_common_cycle(cycles):
    total = math.prod(cycles)
    i = 2

    while i <= max(cycles):
        new_total = total // i
        ok = True
        for a in cycles:
            if new_total % a != 0:
                ok = False
        if ok:
            total = new_total
        else:
            i += 1
    return total

part2 = find_common_cycle([x, y, z])
# part2 = x * y * z
# i = 2
# while i <= max(x, y, z):
#     new_total = part2 // i
#     if new_total % x == 0 and new_total % y == 0 and new_total % z == 0:
#         part2 = new_total
#     else:
#         i += 1

print(f'{part1=}, {part2=}')
