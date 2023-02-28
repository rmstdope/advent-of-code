f = open('input.txt')
str = list(map(int, f.read().splitlines()))

part1 = 0
part2 = 0

for i in range(25, len(str)):
    found = False
    for i1 in range(i - 25, i):
        for i2 in range(i - 25, i):
            if str[i1] != str[i2] and str[i1] + str[i2] == str[i]:
                found = True
    if not found:
        part1 = str[i]
        break

i1 = 0
i2 = 1
s = str[i1] * 2
while s != part1:
    if (s < part1):
        i2 += 1
    else:
        i1 += 1
        i2 = i1 + 1
    s = sum(str[i1:i2])
part2 = max(str[i1:i2]) + min(str[i1:i2])

print(f'{part1=}, {part2=}')
