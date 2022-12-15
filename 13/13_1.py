# https://adventofcode.com/2022/day/13
import os

script_path = os.path.dirname(os.path.realpath(__file__))
input_file = os.path.join(script_path, "input.txt")


def parse_list(slice):
    lst = None
    i = 0
    while i < len(slice):
        c = slice[i]
        shift = 1
        if c == ",":
            pass
        elif c == "[":
            if lst is None:
                lst = []
            else:
                shift, inner_list = parse_list(slice[i:])
                lst.append(inner_list)
        elif c == "]":
            return i + 1, lst
        else:
            elem = int(slice[i])
            lst.append(elem)
        i += shift


# def check_order(left_signal, right_signal) -> bool:
#     for i in range(max(len(left_signal), len(right_signal))):
#         if i == len(left_signal):
#             return True
#         if i == len(right_signal):
#             return False
        
#         left_element = left_signal[i]
#         right_element = right_signal[i]

#         if isinstance(left_element, list) or isinstance(right_element, list):
#             if isinstance(left_element, int):
#                 left_element = [left_element]
#             elif isinstance(right_element, int):
#                 right_element = [right_element]

#             inner_check = check_order(left_element, right_element)
#             if inner_check is not None:
#                 return inner_check
#         else:
#             if left_element != right_element:
#                 return left_element < right_element

    
def check_order(left: list, right: list) -> bool | None:
    for i in range(max(len(left), len(right))):
        if i == len(left):
            return True
        
        if i == len(right):
            return False

        if type(left[i]) is int and type(right[i]) is int:
            if left[i] is not right[i]:
                return left[i] < right[i]
        else:
            result = check_order(left[i] if type(left[i]) is list else [left[i]], right[i] if type(right[i]) is list else [right[i]])

            if result is not None:
                return result


s = 0
with open(input_file, "r") as file:
    pair_count = 0
    total_pair_count = 1
    pair = []
    s = 0
    for line in file:
        if pair_count < 2:
            line = line.strip()
            _, signal = parse_list(line)
            pair.append(signal)
            pair_count += 1  
            
            ssignal = str(signal).replace(" ", "")
            equal = ssignal == line

            print(line, "\n", str(signal), line == str(signal).strip())

            if equal:
                print("EQUAL")
            else:
                print("DIFFER")
            print('\n\n')
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
