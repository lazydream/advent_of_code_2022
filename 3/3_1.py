# https://adventofcode.com/2022/day/3
import os
import string

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, "input.txt")

sum_priorities = 0
with open(input_file, "r") as file:
  for line in file:
    line = line.replace("\n", "")
    line_length = len(line)
    delimiter = line_length // 2
    left, right = line[:delimiter], line[delimiter:]
    left_set = set(left)
    right_set = set(right)
    error_item = left_set & right_set
    priority = string.ascii_letters.index(error_item.pop()) + 1
    sum_priorities += priority

print(sum_priorities)
