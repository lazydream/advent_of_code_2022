# https://adventofcode.com/2022/day/2
import os

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, "input.txt")


winner_matrix = {
  "X": "C",
  "Y": "A",
  "Z": "B"
}

draw_matrix = {
  "A": "X",
  "B": "Y",
  "C": "Z"
}

shape_score = {
  "X": 1,
  "Y": 2,
  "Z": 3
}

def get_outcome(opponent, player):
  if draw_matrix[opponent] == player:
    return 3
  return 6 if winner_matrix[player] == opponent else 0


total_score = 0
with open(input_file, 'r') as file:
  for line in file:
    line = line.replace("\n", "")
    opponent, player = line.split(" ")
    round_score = get_outcome(opponent, player) + shape_score[player]
    total_score += round_score

print(total_score)