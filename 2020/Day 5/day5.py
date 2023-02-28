f = open('input.txt')
str = f.read().splitlines()


def find(start, end, s):
    for c in s:
        if c == 'F' or c == 'L':
            end -= (end - start + 1) >> 1
        else:
            start += (end - start + 1) >> 1
        # print(f'{start=}, {end=}')
    return start


part1 = 0
ids = []
for s in str:
    row = find(0, 127, s[:7])
    col = find(0, 7, s[7:])
    sum = row * 8 + col
    ids.append(sum)
    if sum > part1:
        part1 = sum

ids.sort()
last = ids[0] - 1
for id in ids:
    if id != last + 1:
        part2 = last + 1
    last = id

print(f'{part1=}, {part2=}')
