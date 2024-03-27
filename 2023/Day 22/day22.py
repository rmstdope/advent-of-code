import numpy as np
import copy
import heapq

# f = open('test.txt')
f = open('prod.txt')
strs = f.read().strip().splitlines()

class Brick:
    def __init__(self, num, c1, c2) -> None:
        self.num = num
        self.fallen = False
        s = c1.split(',')
        self.x1 = int(s[0])
        self.y1 = int(s[1])
        self.z1 = int(s[2])
        s = c2.split(',')
        self.x2 = int(s[0])
        self.y2 = int(s[1])
        self.z2 = int(s[2])
        assert(self.x1 <= self.x2)
        assert(self.y1 <= self.y2)
        assert(self.z1 <= self.z2)

    def fall(self, index, bricks):
        blocked = False
        while not blocked:
            blocked = False
            if self.z1 == 1:
                return
            self.z1 -= 1
            self.z2 -= 1
            for i, b in enumerate(bricks):
                if i >= index:
                    continue
                if self.x1 <= b.x2 and self.x2 >= b.x1 and self.y1 <= b.y2 and self.y2 >= b.y1 and  self.z1 <= b.z2 and self.z2 >= b.z1:
                    blocked = True
                    break
            if blocked:
                self.z1 += 1
                self.z2 += 1
            else:
                self.fallen = True

    def doblockedby(self, bricks):
        self.blockedby = []
        for i, b in enumerate(bricks):
            if b == self:
                continue
            if self.x1 <= b.x2 and self.x2 >= b.x1 and self.y1 <= b.y2 and self.y2 >= b.y1 and (self.z1 - 1) <= b.z2 and (self.z2 - 1) >= b.z1:
                self.blockedby.append(b)

    def couldfallif(self, bricks, brick):
        blocked = False
        self.z1 -= 1
        self.z2 -= 1
        if self.z1 == 0:
            blocked = True
        for i, b in enumerate(bricks):
            if b != self and b != brick:
                if self.x1 <= b.x2 and self.x2 >= b.x1 and  self.y1 <= b.y2 and  self.y2 >= b.y1 and  self.z1 <= b.z2 and  self.z2 >= b.z1:
                    blocked = True
        self.z1 += 1
        self.z2 += 1
        return not blocked

bricks = []
for i, s in enumerate(strs):
    s = s.split('~')
    bricks.append(Brick(i, s[0], s[1]))

maxz = 0
for testb in bricks:
    maxz = max(testb.z1, testb.z2, maxz)

# fallen = []
bricks.sort(key=lambda b: b.z1)
for z in range(2, maxz + 1):
    # print(z)
    for i, testb in enumerate(bricks):
        if testb.z1 > z or testb.z2 < z:
            continue
        while testb.fall(i, bricks):
            pass
    bricks.sort(key=lambda b: b.z1)

for testb in bricks:
    testb.doblockedby(bricks)

bricks.sort(key=lambda b: b.z1)

# for z in range(maxz + 1):
#     for testb in bricks:
#         if testb.z1 <= z <= testb.z2:
#             print(testb.num, ' ', end='')
#     print('') 

part1 = 0
for i in range(len(bricks)):    
    # print(i)
    ok = True
    for j in range(len(bricks)):
        if len(bricks[j].blockedby) == 1 and bricks[j].blockedby[0].num == i: 
            ok = False
            break
    if ok:
        part1 += 1

part2 = 0
for i, testb in enumerate(bricks):
    # print(i)
    for b in bricks:
        b.doblockedby(bricks)
    queue = [testb]
    done = [testb]
    for b in bricks:
        if len(b.blockedby) == 0:
            done.append(b)
    while queue:
        removeb = queue.pop()
        for b3 in bricks:
            if b3 in done:
                continue
            if removeb in b3.blockedby:
                b3.blockedby.remove(removeb)
            if len(b3.blockedby) == 0:
                part2 += 1
                queue.append(b3)
                done.append(b3)

print(f'{part1=}, {part2=}')
