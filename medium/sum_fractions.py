import math


def sum_fractions(lst):
    return math.floor(sum([item[0] / item[1] for item in lst]))


print(sum_fractions([[36, 4], [22, 60]]))
print(sum_fractions([[18, 13], [4, 5]]))
