# https://adventofcode.com/2022/day/13
import os
from functools import cmp_to_key
from math import prod

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, "input.txt")

def _parse_list(slice: str) -> list:
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


def cmp(left_signal, right_signal) -> int | None:
    i = 0
    rl = len(right_signal)
    while i < len(left_signal):
        if rl - 1 < i:
            return -1
        left_element = left_signal[i]
        right_element = right_signal[i]

        if isinstance(left_element, list) or isinstance(right_element, list):
            if isinstance(left_element, int):
                left_element = [left_element]
            elif isinstance(right_element, int):
                right_element = [right_element]

            inner_check = cmp(left_element, right_element)
            if inner_check is not None:
                return inner_check
        else:
            if left_element != right_element:
                return 1 if left_element < right_element else -1
        i += 1

    if len(left_signal) < len(right_signal):
        return 1


def parse_signals(input_file_path: str) -> list:
    signals = []
    with open(input_file_path, "r") as file:
        for i, line in enumerate(file):
            if (i + 1) % 3 != 0:
                line = line.strip()
                _, signal = _parse_list(line)
                signals.append(signal)
    return signals


def merge_sort(arr: list, l: int, r: int) -> list:
    if l >= r:
        return
    
    mid = l + (r - l) // 2

    merge_sort(arr, l, mid)
    merge_sort(arr, mid + 1, r)

    ll = arr[l:mid]
    rl = arr[mid:r+1]

    i = j = 0
    k = l

    while (i < len(ll) and j < len(rl)):
        if cmp(ll[i], rl[j]):
            arr[k] = ll[i]
            i += 1
        else:
            arr[k] = rl[i]
            j += 1
        k += 1
    
    while j < len(rl):
        arr[k] = rl[j]
        j += 1
        k += 1
    
    while i < len(ll):
        arr[k] == ll[i]
        i += 1
        k += 1
        


if __name__ == "__main__":
    signals = parse_signals(input_file)
    part_1 = sum([(i+1) // 2 for i in range(1, len(signals), 2) if cmp(signals[i-1], signals[i]) == 1])
    print(part_1)
    dividers = [[[2]], [[6]]]
    signals.extend(dividers)
    signals.sort(key=cmp_to_key(cmp), reverse=True)
    part_2 = prod([i + 1 for i, signal in enumerate(signals) if signal in dividers])
    print(part_2)
