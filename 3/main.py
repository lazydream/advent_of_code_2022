from get_file import *
from string import ascii_letters


elf_dictionary = {key: value for key, value in zip(ascii_letters, range(1, 53))}
input_lines = get_input(get_path(__file__))


#  #1
def common_items():
    sum_ = 0
    for line in input_lines:

        if line:
            halflen = int(len(line) / 2)
            compartment_1 = set(line[:halflen])
            compartment_2 = set(line[halflen:])
            common_item = compartment_1.intersection(compartment_2)
            sum_ += elf_dictionary[common_item.pop()]

    return sum_


#  #2
def elf_three_groups():
    sum_ = 0
    while True:
        try:
            group_1 = set(next(input_lines))
            group_2 = set(next(input_lines))
            group_3 = set(next(input_lines))
            common_item = group_1.intersection(group_2, group_3)
            sum_ += elf_dictionary[common_item.pop()]

        except StopIteration:
            break
    return sum_
