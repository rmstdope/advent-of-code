import numpy as np
import copy
import sympy

# f = open('test.txt')
f = open('prod.txt')
strs = f.read().strip().splitlines()

class Storm:
    def __init__(self, data) -> None:
        data = data.split(' @ ')
        v = data[0].split(', ')
        self.px = int(v[0])
        self.py = int(v[1])
        self.pz = int(v[2])
        v = data[1].split(', ')
        self.vx = int(v[0])
        self.vy = int(v[1])
        self.vz = int(v[2])
        # a * y + b * x + c = 0
        self.a = self.vx
        self.b = -self.vy
        self.c = self.px*self.vy - self.vx*self.py
        # self.c = -a * py - b * px
        self.a = -self.vy
        self.b = self.vx
        self.c = self.px*self.vy - self.vx*self.py

    def collides(self, storm, t1, t2):
        # x = px + vxt
        # y = py + vyt
        # t = y/vy - py/vy
        # x = px + vx*y/vy - vx*py/vy
        # x*vy = px*vy + vx*y - vx*py
        # y*vx - x*vy + (px*vy - vx*py) = 0
        div = (self.a * storm.b - self.b * storm.a)
        if div == 0:
            return False
        xcross = (self.b * storm.c - self.c * storm.b) / div
        ycross = (self.c * storm.a - self.a * storm.c) / div
        tself = (xcross - self.px) / self.vx
        tstorm = (xcross - storm.px) / storm.vx
        if t1 <= xcross <= t2 and t1 <= ycross <= t2 and tself >= 0 and tstorm >=0:
            return True
        return False

storms = []
for s in strs:
    storms.append(Storm(s))

part1 = 0
for i in range(len(strs)):
    for j in range(i + 1, len(strs)):
        # if storms[i].collides(storms[j], 7, 27):
        if storms[i].collides(storms[j], 200000000000000, 400000000000000):
            part1 += 1

equations = []
x, y, z, vx, vy, vz = sympy.symbols("x, y, z, vx, vy, vz")
for i, s in enumerate(storms):
    equations.append((x - s.px) * (s.vy - vy) - (y - s.py) * (s.vx - vx))
    equations.append((y - s.py) * (s.vz - vz) - (z - s.pz) * (s.vy - vy))
    if i > 1:
        answers = []
        for s in sympy.solve(equations):
            ok = True
            for v in s.values():
                if v % 1 != 0:
                    ok = False
            if ok:
                answers.append(s)
        if len(answers) == 1:
            break
    
part2 = answers[0][x] + answers[0][y] + answers[0][z]

print(f'{part1=}, {part2=}')
