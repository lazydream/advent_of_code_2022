from get_file import *


SingleInt = 1 | 2
lst_1 = ['B X', 'C Y', 'A Z', 'A X', 'B Y', 'C Z', 'C X', 'A Y', 'B Z']
lst_2 = ['B X', 'C X', 'A X', 'A Y', 'B Y', 'C Y', 'C Z', 'A Z', 'B Z']


def elf_dictionary(v: int = 1):
    d = {}
    lst = lst_2 if v - 1 else lst_1
    for shapes, points in zip(lst, range(1, 10)):
        d[shapes] = points
    return d


# #1 & #2
def get_sum(task: SingleInt = 1):
    sum_ = 0
    d = elf_dictionary(task)
    for line in get_input(get_path(__file__)):
        if line:
            sum_ += d[line]

    return sum_
