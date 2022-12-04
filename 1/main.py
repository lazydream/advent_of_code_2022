# https://adventofcode.com/2022/day/1
import os

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, "input.txt")
top_3_calories = [0, 0, 0]
with open(input_file, 'r') as file:
  cur_sum = 0

  for line in file:
    if line == "\n":
      if cur_sum > top_3_calories[0]:
        top_3_calories[2] = cur_sum
        top_3_calories[0], top_3_calories[2] = top_3_calories[2], top_3_calories[0]
        top_3_calories[1], top_3_calories[2] = top_3_calories[2], top_3_calories[1]
      elif cur_sum > top_3_calories[1]:
        top_3_calories[2] = cur_sum
        top_3_calories[1], top_3_calories[2] = top_3_calories[2], top_3_calories[1]
      elif cur_sum > top_3_calories[2]:
        top_3_calories[2] = cur_sum
      cur_sum = 0
      continue
    cur_sum += int(line)


print(sum(top_3_calories))