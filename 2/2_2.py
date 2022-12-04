# https://adventofcode.com/2022/day/2
import os

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, "input.txt")


win_choice = {
  "A": "B",
  "B": "C",
  "C": "A"
}

draw_choice = {
  "A": "A",
  "B": "B",
  "C": "C"
}

lose_choice = {
  "A": "C",
  "B": "A",
  "C": "B"
}

shape_score = {
  "A": 1,
  "B": 2,
  "C": 3
}

def round_score(opponent, desired_outcome):
  match desired_outcome:
    case "X":
      total_score = shape_score[lose_choice[opponent]]
    case "Y":
      total_score = 3 + shape_score[draw_choice[opponent]]
    case "Z":
      total_score = 6 + shape_score[win_choice[opponent]]
    
  return total_score

total_score = 0
with open(input_file, 'r') as file:
  for line in file:
    line = line.replace("\n", "")
    opponent, desired_outcome = line.split(" ")
    total_score += round_score(opponent, desired_outcome)
  
print(total_score)