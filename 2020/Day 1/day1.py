f = open('input.txt')
str = list(map(int, f.read().splitlines()))

# part 1
for ix1, x1 in enumerate(str):
    for ix2, x2 in enumerate(str[ix1+1:]):
        if x1 + x2 == 2020:
            print(f'{x1=}, {x2=}, {x1*x2=}')

# part 2
for ix1, x1 in enumerate(str):
    for ix2, x2 in enumerate(str[ix1+1:]):
        for ix3, x3 in enumerate(str[ix2+1:]):
            if x1 + x2 + x3 == 2020:
                print(f'{x1=}, {x2=}, {x3=}, {x1*x2*x3=}')
