import math


def is_sastry(n):
    num = int(str(n) + str(n + 1))
    return math.sqrt(num).is_integer()


print(is_sastry(183))
print(is_sastry(184))
