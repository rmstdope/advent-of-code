import numpy as np
import copy

f = open('input.txt')
strs = f.read().splitlines()
i = 0
valids = []
while strs[i] != '':
    data = strs[i].split(': ')[1]
    data = data.split(' or ')
    vals1 = list(map(int, data[0].split('-')))
    vals2 = list(map(int, data[1].split('-')))
    valids.append(vals1 + vals2)
    i += 1

numFields = i
i += 2
tickets = []
tickets.append(strs[i])

# part 1
i += 3
part1 = 0
for str in strs[i:]:
    ticketValid = True
    for x in list(map(int, str.split(','))):
        valid = False
        for v in valids:
            if (x >= v[0] and x <= v[1]) or (x >= v[2] and x <= v[3]):
                valid = True
        if not valid:
            ticketValid = False
            part1 += x
    if ticketValid:
        tickets.append(str)

# part 2
possibilities = []
fillset = set()
for j in range(numFields):
    fillset.add(j)
for j in range(numFields):
    possibilities.append(copy.deepcopy(fillset))

for str in tickets:
    for ix, x in enumerate(list(map(int, str.split(',')))):
        ok = set()
        for iv, v in enumerate(valids):
            if (x >= v[0] and x <= v[1]) or (x >= v[2] and x <= v[3]):
                ok.add(iv)
        possibilities[ix] = possibilities[ix].intersection(ok)

for j in range(numFields):
    for i in range(numFields):
        if len(possibilities[i]) == 1:
            for k in range(numFields):
                if k != i:
                    possibilities[k] = possibilities[k].difference(
                        possibilities[i])

fields = list(map(int, tickets[0].split(',')))
part2 = 1
for i in range(len(possibilities)):
    if possibilities[i].pop() < 6:
        part2 *= fields[i]

print(f'{part1=}, {part2=}')
