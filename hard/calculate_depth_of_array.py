"""
Calculate Depth of Array

Given a list, write a function to calculate it's depth. Assume a normal list has a depth of 1.

Examples
depth([1, 2, 3, 4]) ➞ 1

depth([1, [2, 3, 4]]) ➞ 2

depth([1, [2, [3, 4]]]) ➞ 3

depth([1, [2, [3, [4]]]]) ➞ 4


"""


def depth(lst):
    for item in lst:
        if isinstance(item, list):
            return 1 + depth(item)

    return + 1


print(depth([1, [2, [3, [4]]]]))
print(depth([1, 2, 3, 4]))
