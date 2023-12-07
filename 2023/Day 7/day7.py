import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
strs = f.read().splitlines()

hands = []
for s in strs:
    data = s.split(' ')
    hands.append([data[0], data[1]])

values = "23456789TJQKA"
values_p2 = "J23456789TQKA"
values_noj = "23456789TQKA"

def get_type_p1(h):
    s = h[0]
    s = sorted(s)
    num = []
    old_c = s[0]
    n = 1
    for c in s[1:]:
        if old_c != c:
            num.append(n)
            n = 1
            old_c = c
        else:
            n += 1
    num.append(n)
    num = sorted(num, reverse=True)
    if num[0] == 5:
        return 1
    elif num[0] == 4:
        return 2
    elif num[0] == 3 and num[1] == 2:
        return 3
    elif num[0] == 3:
        return 4
    elif num[0] == 2 and num[1] == 2:
        return 5
    elif num[0] == 2:
        return 6
    return 7

def get_type(h, p2):
    if not p2:
        return get_type_p1(h)
    min = 100
    l1 = h[0][0]
    l2 = h[0][1]
    l3 = h[0][2]
    l4 = h[0][3]
    l5 = h[0][4]
    if l1 == 'J':
        l1 = values_noj
    if l2 == 'J':
        l2 = values_noj
    if l3 == 'J':
        l3 = values_noj
    if l4 == 'J':
        l4 = values_noj
    if l5 == 'J':
        l5 = values_noj
    for c1 in l1:
        for c2 in l2:
            for c3 in l3:
                for c4 in l4:
                    for c5 in l5:
                        s = c1 + c2 + c3 + c4 + c5
                        v = get_type_p1([s, 0])
                        if v < min:
                            min = v
    return min
 
def is_larger(h1, h2, p2):
    vals = values
    if p2:
        vals = values_p2
    if len(h1) == 2:
        t1 = get_type(h1, p2)
        h1.append(t1)
    else:
        t1 = h1[2]
    if len(h2) == 2:
        t2 = get_type(h2, p2)
        h2.append(t2)
    else:
        t2 = h2[2]
    if t1 < t2:
        return True
    elif t2 == t1:
        for c1,c2 in zip(h1[0], h2[0]):
            if vals.index(c1) > vals.index(c2):
                return True
            elif  vals.index(c1) < vals.index(c2):
                return False
    return False

# print(is_larger(['AAAA7', 0], ['JJJJJ', 0], True))

switched = True
while switched:
    switched = False
    for i in range(len(hands) - 1):
        if is_larger(hands[i], hands[i + 1], False):
            h = hands[i]
            hands[i] = hands[i + 1]
            hands[i + 1] = h
            switched = True

part1 = 0
for i,h in enumerate(hands):
    part1 += (i + 1) * int(h[1])

for h in hands:
    h.pop()

switched = True
while switched:
    switched = False
    for i in range(len(hands) - 1):
        if is_larger(hands[i], hands[i + 1], True):
            h = hands[i]
            hands[i] = hands[i + 1] 
            hands[i + 1] = h
            switched = True

part2 = 0
for i,h in enumerate(hands):
    part2 += (i + 1) * int(h[1])

print(f'{part1=}, {part2=}')
