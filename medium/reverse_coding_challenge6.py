from functools import reduce


def mystery_func(num):
    numbers = [int(x) for x in str(num)]
    return reduce(lambda a, b: a * b, numbers)


print(mystery_func(152))
