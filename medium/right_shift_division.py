import math


def shift_to_right(x, y):
    return math.floor(x / (2 ** y))


print(shift_to_right(80, 3))
print(shift_to_right(-24, 2))
