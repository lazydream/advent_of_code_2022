# https://adventofcode.com/2022/day/11
import os
import re
import math

from collections import deque

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, "input.txt")


class Monkey:
    def __init__(self, items: deque[int], operation: tuple[int, int], test: int, true_case: int, false_case: int):
        self.items = items
        self.operation = (operation[0], operation[1])
        self.test = test
        self.true_case = true_case
        self.false_case = false_case
        self.throw_counter = 0
    
    def throw(self, common_divisor: int, manage_worry_level: bool = True):
        item = self.items.popleft()
        updated_worry_level = self._handle_item(item)
        if manage_worry_level:
            updated_worry_level //= 3
        updated_worry_level %= common_divisor
        recipient = self.true_case if updated_worry_level % self.test == 0 else self.false_case
        self.throw_counter += 1
        return recipient, updated_worry_level
    
    def catch(self, item: int):
        self.items.append(item)
    
    def _handle_item(self, i: int):
        part = i if self.operation[1] == "old" else int(self.operation[1])
        if self.operation[0] == "+":
            i += part
        elif self.operation[0] == "*":
            i *= part
        return i


def parse_monkeys() -> dict[int, Monkey]:
    monkeys: dict[int, Monkey] = dict()
    with open(input_file, "r") as file:
        items = []
        monkey_id = operation = test = true_case = false_case = None
        for i, line in enumerate(file):
            line = re.sub(r'[:,\n]', "", line.strip())
            line = line.split(" ")
            if i % 7 == 0:
                monkey_id = int(line[1])
            elif i % 7 == 1:
                items = deque(map(int, line[2:]))
            elif i % 7 == 2:
                operation = line[4], line[5]
            elif i % 7 == 3:
                test = int(line[3])
            elif i % 7 == 4:
                true_case = int(line[5])
            elif i % 7 == 5:
                false_case = int(line[5])
                monkey = Monkey(items, operation, test, true_case, false_case)
                monkeys[monkey_id] = monkey
                items = []
                monkey_id = operation = test = true_case = false_case = None
    return monkeys


class Game:
    def __init__(self, rounds: int, unmanageable_worry: bool = False) -> None:
        self.monkeys = parse_monkeys()
        self.rounds = rounds
        self.unmanageable_worry = unmanageable_worry
        self.common_divisor = math.prod([monkey.test for monkey in self.monkeys.values()])
    
    def get_monkey_business(self):
        for _ in range(self.rounds):
            for monkey in self.monkeys.values():
                 while monkey.items:
                    recipient, item_worry_level = monkey.throw(self.common_divisor, not self.unmanageable_worry)
                    self.monkeys[recipient].catch(item_worry_level)
        monkey_throws = sorted([monkey.throw_counter for monkey in self.monkeys.values()], reverse=True)
        monkey_business = monkey_throws[0] * monkey_throws[1]
        return monkey_business

# Part 1
game_1 = Game(20)
print(game_1.get_monkey_business())

# Part 2
game_2 = Game(10000, True)
print(game_2.get_monkey_business())
