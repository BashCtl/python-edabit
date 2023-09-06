import itertools


def max_product(lst):
    return max([triplet[0] * triplet[1] * triplet[2] for triplet in itertools.combinations(lst, 3)])


def min_product(lst):
    return min([triplet[0] * triplet[1] * triplet[2] for triplet in itertools.combinations(lst, 3)])


print(max_product([-8, -9, 1, 2, 7]))
print(min_product([-5, -3, -1, 0, 4]))