"""
Squishing a List
Write a function that squishes a list from the left or the right.

Examples
squish([1, 2, 3, 4, 5], "left")
➞ [[1, 2, 3, 4, 5], [3, 3, 4, 5], [6, 4, 5], [10, 5], [15]]

squish([1, 2, 3, 4, 5], "right")
➞ [[1, 2, 3, 4, 5], [1, 2, 3, 9], [1, 2, 12], [1, 14], [15]]

squish([1, 0, 2, -3], "left")
➞ [[1, 0, 2, -3], [1, 2, -3], [3, -3], [0]]

squish([1, 0, 2, -3], "right")
➞ [[1, 0, 2, -3], [1, 0, -1], [1, -1], [0]]
Notes
Squishing from the left is to successively sum the first two elements of a list (shortening the list in the process).
Squishing from the right is to successively sum the last two elements of a list.
Include the original list as the first element in either squish.
Return an empty list if the input is an empty list.

"""

from unittest import TestCase


def squish(lst, d, result=None):
    if not lst:
        return lst
    if result is None:
        result = [lst]
    if len(lst) == 1:
        return result
    lst = lst.copy()
    if d == "left":
        lst[:2] = [lst[0] + lst[1]]
    elif d == "right":
        lst[-2:] = [lst[-2] + lst[-1]]
    result.append(lst)
    return squish(lst, d, result)


TestCase().assertEqual(squish([1, 2, 3, 4, 5], "left"), [[1, 2, 3, 4, 5], [3, 3, 4, 5], [6, 4, 5], [10, 5], [15]])
TestCase().assertEqual(squish([1, 0, 2, -3], "left"), [[1, 0, 2, -3], [1, 2, -3], [3, -3], [0]])
TestCase().assertEqual(squish([4, 9, -3, 2, 5], "left"), [[4, 9, -3, 2, 5], [13, -3, 2, 5], [10, 2, 5], [12, 5], [17]])
TestCase().assertEqual(squish([8, -7, 6, 1, 0, 2], "left"),
                       [[8, -7, 6, 1, 0, 2], [1, 6, 1, 0, 2], [7, 1, 0, 2], [8, 0, 2], [8, 2], [10]])
TestCase().assertEqual(squish([8, 7], "left"), [[8, 7], [15]])
TestCase().assertEqual(squish([8], "left"), [[8]])
TestCase().assertEqual(squish([], "left"), [])

TestCase().assertEqual(squish([1, 2, 3, 4, 5], "right"), [[1, 2, 3, 4, 5], [1, 2, 3, 9], [1, 2, 12], [1, 14], [15]])
TestCase().assertEqual(squish([1, 0, 2, -3], "right"), [[1, 0, 2, -3], [1, 0, -1], [1, -1], [0]])
TestCase().assertEqual(squish([4, 9, -3, 2, 5], "right"), [[4, 9, -3, 2, 5], [4, 9, -3, 7], [4, 9, 4], [4, 13], [17]])
TestCase().assertEqual(squish([8, -7, 6, 1, 0, 2], "right"),
                       [[8, -7, 6, 1, 0, 2], [8, -7, 6, 1, 2], [8, -7, 6, 3], [8, -7, 9], [8, 2], [10]])
TestCase().assertEqual(squish([8, 7], "right"), [[8, 7], [15]])
TestCase().assertEqual(squish([8], "right"), [[8]])
TestCase().assertEqual(squish([], "right"), [])
