f = open('input.txt')
str = f.read().splitlines()

part1 = 0
part2 = 0
for s in str:
    num, ch, pwd = s.split(' ')
    n1, n2 = map(int, num.split('-'))
    ch = ch[0]
    occ = pwd.count(ch)
    if occ <= n2 and occ >= n1:
        part1 += 1
    if (pwd[n1 - 1] == ch) + (pwd[n2 - 1] == ch) == 1:
        part2 += 1

print(f'{part1=}: {part2=}')
