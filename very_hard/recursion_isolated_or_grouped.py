"""
Recursion: Isolated or Grouped?

Write a function that extracts the max value of a number in a list.
If there are two or more max values, return it as a list, otherwise, return the number.
This process could be relatively easy with some of the built-in list functions but the required approach is recursive.

Examples
iso_group([31, 7, 2, 13, 7, 9, 10, 13]) ➞ 31

iso_group([1, 3, 9, 5, 1, 7, 9, -9]) ➞ [9, 9]

iso_group([97, 19, -18, 97, 36, 23, -97]) ➞ [97, 97]

iso_group([-31, -7, -13, -7, -9, -13]) ➞ [-7, -7]

iso_group([-1, -3, -9, -5, -1, -7, -9, -9]) ➞ [-1, -1]

iso_group([107, 19, -18, 79, 36, 23, 97]) ➞ 107
"""


def iso_group(lst: list, result=None):
    if not lst:
        return result
    elif result is None or lst[0] > result:
        return iso_group(lst[1:], lst[0])
    elif lst[0] == result:
        return [result] + [iso_group(lst[1:], result)]
    else:
        return iso_group(lst[1:], result)


from unittest import TestCase

num_vector, res_vector = [[
    [31, 7, 2, 13, 7, 9, 10, 13],
    [1, 3, 9, 5, 1, 7, 9, -9],
    [97, 19, -18, 97, 36, 23, -97],
    [-31, -7, -13, -7, -9, -13],
    [-1, -3, -9, -5, -1, -7, -9, -9],
    [107, 19, -18, 79, 36, 23, 97],
    [10, -6, -3, 38, 12, 72, 59, 32]],
    [31, [9, 9], [97, 97], [-7, -7], [-1, -1], 107, 72]]
for i, r in enumerate(num_vector):
    TestCase().assertEqual(iso_group(r), res_vector[i])
