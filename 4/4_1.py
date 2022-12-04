# https://adventofcode.com/2022/day/4
import os

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, "input.txt")

def range_contains(left_range, right_range):
  inside = lambda r: left_range[0] <= r <= left_range[1]
  if inside(right_range[0]) and inside(right_range[1]):
    return True
  return False

critical_pairs = 0
with open(input_file, "r") as file:
  for line in file:
    line = line.replace("\n", "")
    left_range, right_range = map(lambda r: r.split("-"), line.split(","))
    left_range = [int(r) for r in left_range]
    right_range = [int(r) for r in right_range]
    
    if range_contains(left_range, right_range) or range_contains(right_range, left_range):
      critical_pairs += 1

print(critical_pairs)
