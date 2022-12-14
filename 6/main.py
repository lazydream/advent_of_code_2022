from get_file import *


def gline():
    for line in get_input(get_path(__file__)):
        for letter in line:
            yield letter


def nof_distinct(n: int) -> int:

    result = 0
    counter = n - 1
    lasts_ = []
    lines = gline()

    for _ in range(n - 1):
        lasts_.append(next(lines))

    for i in lines:
        counter += 1
        lasts_.append(i)
        if len(set(lasts_)) == n:
            result = counter
            break
        lasts_ = lasts_[1:]

    return result


print(nof_distinct(4))
print(nof_distinct(14))
