import math
import itertools

def prime_factors(n):
    while n % 2 == 0:
        yield 2
        n = n // 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i== 0:
            yield i
            n = n // i
    if n > 2:
        yield n

def divisors(number):
    primes = list(prime_factors(number))
    x = [math.prod(l) for l in itertools.combinations(primes, 1)]
    for i in range(2, len(primes) + 1):
        x += [math.prod(l) for l in itertools.combinations(primes, i)]
    x = list(set(x))
    x.append(1)
    x.sort()
    return x

def filter_coords(coords, max_x, max_y):
    return list(filter(lambda x: x[0] >= 0 and x[0] <= max_x and x[1] >= 0 and x[1] <= max_y, coords))

def split_in_chunks(data):
    return [d.split('\n') for d in data.split('\n\n')]

def try_int(x):
    try:
        int(x)
        return int(x)
    except:
        return x

def split_lines_and_words(data, to_int=False):
    out = [line.split() for line in data.splitlines()]
    if to_int:
        out = [[try_int(x) for x in line] for line in out]
    return out

def make_grid(data, to_int=False):
    grid = []
    for line in data.splitlines():
        row = []
        for c in line:
            if to_int:
                row.append(try_int(c))
            else:
                row.append(c)
        grid.append(row)
    return grid

class VM:
    def __init__(self, program, num_regs, debug_print_every=-1):
        self.program = program
        self.regs = [0] * num_regs
        self.debug_print_every = debug_print_every
        self.reset()
        
    def reset(self):
        self.pc = 0
        self.executed = 0
        self.visited = set()
        self.finished = False
        for i in range(len(self.regs)):
            self.regs[i] = 0

    def execute(self):
        raise NotImplementedError()

    def jump(self, offset):
        self.pc += offset - 1

    def run(self):
        while not self.finished:
            instr = self.program[self.pc]
            self.pc += 1
            self.execute(instr)
            self.executed += 1
            if self.debug_print_every > 0 and self.executed % self.debug_print_every == 0:
                print(f'Regs: {self.regs}, PC: {self.pc}, Executed: {self.executed}')
            self.finished = self.pc >= len(self.program)
        return self.regs

