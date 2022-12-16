from get_file import *
from math import ceil


class Point:

    def __init__(self):
        self.horizontal = 0
        self.vertical = 0

    def current_coordinates(self):
        return self.horizontal, self.vertical


class H(Point):

    def step(self, command: str):
        match command:
            case 'R':
                self.horizontal += 1
            case 'L':
                self.horizontal -= 1
            case 'U':
                self.vertical += 1
            case 'D':
                self.vertical -= 1


class T(Point):

    def __init__(self, pair: H):
        super().__init__()
        self.pair = pair
        self.history = set()
        self.history.add((0, 0))

    @staticmethod
    def abs_round(num):
        if num < 0:
            if round(num) - num == 0.5:
                return round(num) - 1
        return ceil(num)

    @staticmethod
    def square(x1: int, y1: int, x2: int, y2: int) -> int:
        return (x1 - x2) ** 2 + (y1 - y2) ** 2

    def step(self):
        x, y = self.current_coordinates()
        x_pair, y_pair = \
            self.pair.current_coordinates()
        square = self.square(x, y, x_pair, y_pair)
        if square > 2:
            self.vertical += self.abs_round((y_pair - y) / 2)
            self.horizontal += self.abs_round((x_pair - x) / 2)

        self.history.add(self.current_coordinates())


input_lines = get_input(get_path(__file__))
head = H()
tail = T(head)

for line in input_lines:
    command, steps = line.split()
    for _ in range(int(steps)):
        head.step(command)
        tail.step()

print(len(tail.history))
