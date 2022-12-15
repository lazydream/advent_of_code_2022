# https://adventofcode.com/2022/day/13
import os

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, "input.txt")


def _parse_list(slice):
    lst = None
    i = 0
    n = []
    while i < len(slice):
        c = slice[i]
        shift = 1
        if c == ",":
            if n:
                lst.append(int("".join(n)))
            n = []
        elif c == "[":
            if lst is None:
                lst = []
            else:
                shift, inner_list = _parse_list(slice[i:])
                lst.append(inner_list)
        elif c == "]":
            if n:
                lst.append(int("".join(n)))
            return i + 1, lst
        else:
            n.append(c)
        i += shift


def check_order(left_signal, right_signal) -> bool:
    i = 0
    rl = len(right_signal)
    while i < len(left_signal):
        if rl - 1 < i:
            return False
        left_element = left_signal[i]
        right_element = right_signal[i]

        if isinstance(left_element, list) or isinstance(right_element, list):
            if isinstance(left_element, int):
                left_element = [left_element]
            elif isinstance(right_element, int):
                right_element = [right_element]

            inner_check = check_order(left_element, right_element)
            if inner_check is not None:
                return inner_check
        else:
            if left_element != right_element:
                return left_element < right_element
        i += 1

    if len(left_signal) < len(right_signal):
        return True


s = 0
with open(input_file, "r") as file:
    pair_count = 0
    total_pair_count = 1
    pair = []
    s = 0
    for line in file:
        if pair_count < 2:
            line = line.strip()
            _, signal = _parse_list(line)
            pair.append(signal)
            pair_count += 1
        else:
            if check_order(pair[0], pair[1]):
                s += total_pair_count

            total_pair_count += 1
            pair_count = 0
            pair = []
            pass
print(s)


if __name__ == "__main__":
    pass
