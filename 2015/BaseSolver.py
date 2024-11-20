import os
from aocd.models import Puzzle

class BaseSolver(Puzzle):
    def __init__(self, filename):
        path = os.getcwd().split('\\')
        year = int(path[len(path) - 1])
        day = int(os.path.basename(filename)[3:-3])
        Puzzle.__init__(self, year=year, day=day)
        print(f'Puzzle {year}/{day}: {self.title}')

    def solve_part_1(self):
        print(f'Solving Part 1')
        # First solve all examples
        examples = self.examples
        try:
            examples = self.get_examples()
        except AttributeError:
            pass
        for i,e in enumerate(examples):
            if e.answer_a != None:
                answer = self.solve(False, e.input_data)
                if answer != e.answer_a:
                    print(f'Example {i}: Got {answer} but was expecting {e.answer_a}')
                    exit(code=1)
                else:
                    print(f'Solved example {i}')

        # Next solve the problem
        answer = self.solve(False, self.input_data)
        print(f'Submitting answer: {answer}')
        self.answer_a = answer

    def solve_part_2(self):
        print(f'Solving Part 2')
        # First solve all examples
        examples = self.examples
        try:
            examples = self.get_examples()
        except AttributeError:
            pass
        for i,e in enumerate(examples):
            if e.answer_b != None:
                answer = self.solve(True, e.input_data)
                if answer != e.answer_b:
                    print(f'Example {i}: Got {answer} but was expecting {e.answer_b}')
                    exit(code=1)
                else:
                    print(f'Solved example {i}')

        # Next solve the problem
        answer = self.solve(True, self.input_data)
        print(f'Submitting answer: {answer}')
        self.answer_b = answer
