import numpy as np
import copy

#f = open('test.txt')
f = open('prod.txt')
str = f.read().split(',')

class Intcode:
    def __init__(self, str):
        self.s = [eval(i) for i in str]
        self.input = []
        self.used_input = []
        self.ip = 0
        self.base_offset = 0
        self.exited = False

    def save(self):
        self.s_save = copy.deepcopy(self.s)
        self.input_save = copy.deepcopy(self.input)
        self.used_input_save = copy.deepcopy(self.used_input)
        self.ip_save = self.ip
        self.base_offset_save = self.base_offset
        self.exited_save = self.exited

    def restore(self):
        self.s = copy.deepcopy(self.s_save)
        self.input = copy.deepcopy(self.input_save)
        self.used_input = copy.deepcopy(self.used_input_save)
        self.ip = self.ip_save
        self.base_offset = self.base_offset_save
        self.exited = self.exited_save

    def add_input(self, inp):
        self.input.append(inp)

    def get_num_inputs(self):
        return len(self.input)

    def set_memory(self, address, value):
        self.s[address] = value

    def get_mode(self, num):
        if num == 0:
            return (self.s[self.ip] // 100) % 10
        elif num == 1:
            return (self.s[self.ip] // 1000) % 10
        return (self.s[self.ip] // 10000) % 10

    def get_parameter(self, num):
        if self.get_mode(num) == 0:
            addr = self.s[self.ip + num + 1]
        elif self.get_mode(num) == 1:
            addr = self.ip + num + 1
        else:
            addr = self.base_offset + self.s[self.ip + num + 1]
        while addr > len(self.s) - 1:
            self.s.append(0)
        return self.s[addr]

    def set_parameter(self, num, val):
        if self.get_mode(num) == 0:
            addr = self.s[self.ip + num + 1]
        elif self.get_mode(num) == 1:
            addr = self.ip + num + 1
        else:
            addr = self.base_offset + self.s[self.ip + num + 1]
        while addr > len(self.s) - 1:
            self.s.append(0)
        self.s[addr] = val

    def run_to_output(self):
        return self.run(True)

    def run_to_finish(self):
        return self.run(False)

    def run(self, run_to_output):
        output = []
        op = 0
        while op != 99:
            op = self.s[self.ip] % 100
            match (op):
                case 1:
                    v1 = self.get_parameter(0)
                    v2 = self.get_parameter(1)
                    self.set_parameter(2, v1 + v2)
                    self.ip += 4
                case 2:
                    v1 = self.get_parameter(0)
                    v2 = self.get_parameter(1)
                    self.set_parameter(2, v1 * v2)
                    self.ip += 4
                case 3:
                    self.set_parameter(0, self.input[0])
                    self.used_input.append(self.input.pop(0))
                    self.ip += 2
                case 4:
                    output.append(self.get_parameter(0))
                    self.ip += 2
                    if run_to_output:
                        return output
                case 5:
                    if (self.get_parameter(0) != 0):
                        self.ip = self.get_parameter(1)
                    else:
                        self.ip += 3
                case 6:
                    if (self.get_parameter(0) == 0):
                        self.ip = self.get_parameter(1)
                    else:
                        self.ip += 3
                case 7:
                    if self.get_parameter(0) < self.get_parameter(1):
                        self.set_parameter(2, 1)
                    else:
                        self.set_parameter(2, 0)
                    self.ip += 4
                case 8:
                    if self.get_parameter(0) == self.get_parameter(1):
                        self.set_parameter(2, 1)
                    else:
                        self.set_parameter(2, 0)
                    self.ip += 4
                case 9:
                    self.base_offset += self.get_parameter(0)
                    self.ip += 2
                case 99:
                    self.ip += 1
                    self.exited = True
        return output

part1 = 0
part2 = 0
num_blocks = 1

def setup_game():
    global i
    global num_blocks
    global part1
    global data
    global paddle_pos
    i = Intcode(str)
    num_blocks = 0
    data = []
    while not i.exited:
        output = i.run_to_output()
        if len(output) != 0:
            x = output[0];
            y = i.run_to_output()[0]
            t = i.run_to_output()[0]
            data.append([x, y, t])
            #print(f'{x=}, {y=}, {t=}')
            if t == 2:
                num_blocks += 1
            if t == 3:
                paddle_pos = x
    part1 = num_blocks

def draw(data):
    minx = 0
    miny = 0
    maxx = 0
    maxy = 0
    for d in data:
        if d[0] < minx:
            minx = d[0]
        if d[0] > maxx:
            maxx = d[0]
        if d[1] < miny:
            miny = d[0]
        if d[1] > maxy:
            maxy = d[0]
    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            if [x, y, 1] in data:
                print('#', end='')
            elif [x, y, 2] in data:
                print('$', end='')
            elif [x, y, 3] in data:
                print('=', end='')
            elif [x, y, 4] in data:
                print('*', end='')
            else:
                print(' ', end='')
        print(' ')

setup_game()
#draw(data)
score = 0
i.set_memory(0, 2)
i.exited = False
while num_blocks > 0:
    i.add_input(0)
    score_updated = False
    while num_blocks > 0 or not score_updated:
        output = i.run_to_output()
        if len(output) != 0:
            x = output[0]
            y = i.run_to_output()[0]
            t = i.run_to_output()[0]
            if x == -1:
                if t > 0:
                    score = t
                    # print('Score is ', score)
                    score_updated = True
            else:
                if [x, y, 2] in data:
                    num_blocks -= 1
                    # print(num_blocks, ' blocks remaining')
                    score_updated = False
                    data.remove([x, y, 2])
                if [x, y, 3] in data:
                    data.remove([x, y, 3])
                if [x, y, 4] in data:
                    data.remove([x, y, 4])
                if t != 0:
                    data.append([x, y, t])
                if t == 3:
                    # print('Paddle pos is ', x, ', ', y)
                    paddle_pos = x
                if t == 4:
                    # print('Ball pos is   ', x, ', ', y)
                    if x < paddle_pos:
                        i.add_input(-1)
                    elif x > paddle_pos:
                        i.add_input(1)
                    else:
                        i.add_input(0)
                if y == 22 and t == 4:
                    ball_pos = x
                    break
    # draw(data)
    # print('Score is ', score)
    # print(num_blocks, ' blocks remaining')

part2 = score

print(f'{part1=}, {part2=}')
