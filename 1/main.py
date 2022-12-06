from get_file import *


# #1
def count_calories():
    max_calories = 0
    temp_max = 0

    for line in get_input(get_path(__file__)):
        if line:
            temp_max += int(line)
        else:
            max_calories = max(max_calories, temp_max)
            temp_max = 0
    return max_calories


# #2
def count_top3():

    calories_data = []
    temp_max = 0

    for line in get_input(get_path(__file__)):
        if line:
            temp_max += int(line)
        else:
            calories_data.append(temp_max)
            temp_max = 0

    return sum(sorted(calories_data, reverse=True)[:3])


# #2 O(n) solution
def count_top_3():

    top_1, top_2, top_3 = 0, 0, 0
    temp_max = 0

    def rerank(value: int):

        nonlocal top_1, top_2, top_3
        if value >= top_1:
            top_3, top_2, top_1 = top_2, top_1, value
        elif value >= top_2:
            top_3, top_2 = top_2, value
        elif value >= top_3:
            top_3 = value

    for line in get_input(get_path(__file__)):
        if line:
            temp_max += int(line)
        else:
            rerank(temp_max)
            temp_max = 0

    return sum((top_1, top_2, top_3))
