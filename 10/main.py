from get_file import *


class CPU:

    def __init__(self):
        self.register_value = 1
        self.cycles = 1
        self.strength = 0

    def do_cycle(self, value=None):
        if value:
            self.register_value += int(value)
        self.cycles += 1
        if (self.cycles + 20) % 40 == 0:
            self.strength += self.cycles * self.register_value
        print(self.cycles, self.register_value)

    def instruction(self, line):
        instructions = line.split()
        self.do_cycle()
        if len(instructions) == 2:
            self.do_cycle(instructions[-1])


input_lines = get_input(get_path(__file__))
cpu = CPU()
for line in input_lines:
    cpu.instruction(line)

print(cpu.strength)
