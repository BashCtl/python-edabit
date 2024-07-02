"""
Replace With Next Largest Number


Write a function that replaces each integer with the next largest in the list.

Examples
replace_next_largest([5, 7, 3, 2, 8]) ➞ [7, 8, 5, 3, -1]

replace_next_largest([2, 3, 4, 5]) ➞ [3, 4, 5, -1]

replace_next_largest([1, 0, -1, 8, -72]) ➞ [8, 1, 0, -1, -1]
Notes
Replace the maximum with -1.
Elements in the list will be unique.
You don't have to swap the elements.

"""

from unittest import TestCase


def replace_next_largest(lst):
    sorted_lst = sorted(lst)
    next_largest = {}
    for i in range(len(sorted_lst) - 1):
        next_largest[sorted_lst[i]] = sorted_lst[i + 1]
    next_largest[sorted_lst[-1]] = -1

    result = [next_largest[num] for num in lst]
    return result


TestCase().assertEqual(replace_next_largest([5, 7, 3, 2, 8]), [7, 8, 5, 3, -1])
TestCase().assertEqual(replace_next_largest([4, 1, 6, -7, -8, 2]), [6, 2, -1, 1, -7, 4])
TestCase().assertEqual(replace_next_largest([2, 3, 4, 5]), [3, 4, 5, -1])
TestCase().assertEqual(replace_next_largest([1, 0, -1, 8, -72]), [8, 1, 0, -1, -1])
