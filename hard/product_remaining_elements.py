"""
Product of Remaining Elements

Write a function that returns True if you can partition
a list into one element and the rest, such that this element
is equal to the product of all other elements excluding itself.

Examples
can_partition([2, 8, 4, 1]) ➞ True
# 8 = 2 x 4 x 1

can_partition([-1, -10, 1, -2, 20]) ➞ False

can_partition([-1, -20, 5, -1, -2, 2]) ➞ True

Notes
The list may contain duplicates.
Multiple solutions can exist, any solution is sufficient to return True.

"""

from functools import reduce


def can_partition(lst):
    zeros = lst.count(0)
    if zeros == 1:
        return False
    for num in lst:
        temp = lst.copy()
        temp.remove(num)
        product = reduce(lambda x, y: x * y, temp)
        if product == num:
            return True
    return False


print(can_partition([2, 8, 4, 1]))
print(can_partition([-1, -10, 1, -2, 20]))
print(can_partition([0, 0, 1, 1]))
