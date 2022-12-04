# https://adventofcode.com/2022/day/3
import os
import string

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, "input.txt")

sum_priorities = 0
with open(input_file, "r") as file:
  prev_lines = []
  for line in file:
    line = line.replace("\n", "")
    if len(prev_lines) == 2:
      badge = set(line) & set(prev_lines[0]) & set(prev_lines[1])
      prev_lines = []
      priority = string.ascii_letters.index(badge.pop()) + 1
      sum_priorities += priority
    else:
      prev_lines.append(set(line))

print(sum_priorities)
