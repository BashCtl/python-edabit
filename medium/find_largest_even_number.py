"""
Find The Largest Even Number


Write a function that finds the largest even number in a list. Return -1 if not found. The use of built-in functions max() and sorted() are prohibited.

Examples
largest_even([3, 7, 2, 1, 7, 9, 10, 13]) ➞ 10

largest_even([1, 3, 5, 7]) ➞ -1

largest_even([0, 19, 18973623]) ➞ 0
Notes
Consider using the modulo operator % or the bitwise and operator &.
"""

from inspect import getsource as src
from re import findall, M
from unittest import TestCase


def largest_even(lst):
    result = -1
    for item in lst:
        if item % 2 == 0 and item > result:
            result = item
    return result


def no_builtin_max(fn):
    try:
        return not len(findall('max', src(fn), M))
    except OSError:
        return True


TestCase().assertNotEquals(no_builtin_max(largest_even), False, 'The use of max() is prohibited!')

num_vector, res_vector = [[
    [3, 7, 2, 1, 7, 9, 10, 13], [1], [22], [13, 5, 7, 9], [3, 19, 18973623, 2]],
    [10, -1, 22, -1, 2]]
for i, r in enumerate(num_vector): TestCase().assertEqual(largest_even(r), res_vector[i])
