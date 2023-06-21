from collections import Counter


def sum_common(lst1, lst2, lst3):
    intersection = Counter(lst1) & Counter(lst2) & Counter(lst3)
    return sum([k * v for k, v in intersection.items()])


print(sum_common([1, 2, 2, 3], [5, 3, 2, 2], [7, 3, 2, 2]))
print(sum_common([1, 2, 3], [5, 3, 2], [7, 3, 2]))
