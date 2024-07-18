"""
Check If Lines Are Parallel

Given two lines, determine whether or not they are parallel.

Lines are represented by a list [a, b, c], which corresponds to the line ax+by=c.

Examples
lines_are_parallel([1, 2, 3], [1, 2, 4]) ➞ True
# x+2y=3 and x+2y=4 are parallel.

lines_are_parallel([2, 4, 1], [4, 2, 1]) ➞ False
# 2x+4y=1 and 4x+2y=1 are not parallel.

lines_are_parallel([0, 1, 5], [0, 1, 5]) ➞ True
# Lines are parallel to themselves.
Notes
Two lines are parallels if they have the same slope. If the slopes are different, the lines are not parallel.
All test cases use valid input (no lists of the wrong size, for example).
All coefficients will be integers (whole numbers).

"""
from unittest import TestCase


def lines_are_parallel(line1, line2):
    a1, b1, _ = line1
    a2, b2, _ = line2

    return a1 * b2 == a2 * b1


TestCase().assertEqual(lines_are_parallel([1, 2, 3], [1, 2, 4]), True, "Given example 1.")
TestCase().assertEqual(lines_are_parallel([2, 4, 1], [4, 2, 1]), False, "Given example 2.")
TestCase().assertEqual(lines_are_parallel([0, 1, 5], [0, 1, 5]), True, "Given example 3.")
TestCase().assertEqual(lines_are_parallel([2, 5, 0], [20, 50, 10]), True)
TestCase().assertEqual(lines_are_parallel([2, 5, 0], [-200, -500, 10]), True)
TestCase().assertEqual(lines_are_parallel([400000, 1, 0], [400000, 2, 0]), False)
TestCase().assertEqual(lines_are_parallel([800, 20, 0], [40, 20, 0]), False)
TestCase().assertEqual(lines_are_parallel([400000, 1, 0], [800000, 2, 100000]), True)
TestCase().assertEqual(lines_are_parallel([-5, 7, 100000], [5, -7, -200000]), True)
