f = open('input.txt')
str = f.read().splitlines()

bags = {}
for s in str:
    c = s.split('bags')[0].strip()
    b = s.split('contain ')[1].rstrip('.')
    lst = b.split(', ')
    a = []
    for l in lst:
        if (l != 'no other bags'):
            num = l[:l.find(' ')]
            l = l[l.find(' ') + 1:l.rfind(' ')]
            a.append((l, int(num)))
    bags[c] = a

check = set()
found = set()
check.add('shiny gold')
while len(check) != 0:
    bag_check = check.pop()
    for q, bag in bags.items():
        for c, i in bag:
            if c == bag_check:
                if q not in check:
                    check.add(q)
                    found.add(q)


check = set()
check.add(('shiny gold', 1))
numbags = 0
while len(check) != 0:
    bag_check, num = check.pop()
    for bag, containlist in bags.items():
        if bag == bag_check:
            for addbag, addnum in containlist:
                check.add((addbag, addnum * num))
                numbags += addnum * num


part1 = len(found)
part2 = numbags

print(f'{part1=}, {part2=}')
