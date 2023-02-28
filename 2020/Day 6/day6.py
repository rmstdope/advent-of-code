f = open('input.txt')
str = f.read().splitlines()

part1 = 0
part2 = 0

dic = {}
num = 0
for s in str:
    if s == '':
        part1 += len(dic)
        for y, d in dic.items():
            if (d == num):
                part2 += 1
        dic = {}
        num = 0
    else:
        num += 1
        for c in s:
            dic[c] = 1 + (dic[c] if dic.get(c) else 0)

part1 += len(dic)

for y, d in dic.items():
    if (d == num):
        part2 += 1


print(f'{part1=}, {part2=}')
