from functools import reduce


def boolean_and(lst):
    return reduce(lambda x, y: x and y, lst)


def boolean_or(lst):
    return reduce(lambda x, y: x or y, lst)


def boolean_xor(lst):
    return reduce(lambda x, y: x ^ y, lst)


print(boolean_and([True, True, False, True]))
print(boolean_and([False, True, False, True]))

print(boolean_or([True, True, False, False]))

print(boolean_xor([True, True, False, False]))
