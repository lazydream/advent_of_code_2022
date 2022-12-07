from get_file import *


input_lines = get_input(get_path(__file__))


def get_bound(bound: str):
    return map(int, bound.split('-'))


def compare(range_: list):

    left, right = range_
    left_low, left_high = get_bound(left)
    right_low, right_high = get_bound(right)
    return left_low >= right_low and left_high <= right_high \
        or left_low <= right_low and left_high >= right_high


# #1
def whole_overlap():
    sum_ = 0
    for pair in input_lines:
        sum_ += compare(pair.split(','))
    return sum_


# #2
def partial_overlap():
    sum_ = 0
    for pair in input_lines:
        both = list(map(lambda x: list(get_bound(x)), pair.split(',')))
        if not (both[0][1] < both[1][0] or both[0][0] > both[1][1]):
            sum_ += 1
    return sum_
