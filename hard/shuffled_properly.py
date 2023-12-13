from unittest import TestCase

"""
Shuffled Properly?

Given a list of 10 numbers, return whether or not the list 
is shuffled sufficiently enough. In this case, if 3 or 
more numbers appear consecutively (ascending or descending), return False.

Examples
is_shuffled_well([1, 2, 3, 5, 8, 6, 9, 10, 7, 4]) ➞ False
# 1, 2, 3 appear consecutively

is_shuffled_well([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]) ➞ False
# 9, 8, 7, 6 appear consecutively

is_shuffled_well([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]) ➞ True
# No consecutive numbers appear

is_shuffled_well([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]) ➞ True
# No consecutive numbers appear

Notes
Only steps of 1 in either direction count as consecutive 
(i.e. a sequence of odd and even numbers would count as being properly shuffled (see example #4)).
You will get numbers from 1-10.

"""


def is_shuffled_well(lst):
    for i in range(len(lst) - 3):
        if (abs(lst[i] - lst[i + 1]) == 1
                and abs(lst[i + 1] - lst[i + 2]) == 1):
            return False
    return True


TestCase().assertEqual(is_shuffled_well([1, 2, 3, 5, 8, 6, 9, 10, 7, 4]), False, "1, 2, 3 appear consecutively.")
TestCase().assertEqual(is_shuffled_well([3, 5, 1, 9, 8, 7, 6, 4, 2, 10]), False, "9, 8, 7, 6 appear consecutively.")
TestCase().assertEqual(is_shuffled_well([1, 5, 3, 8, 10, 2, 7, 6, 4, 9]), True, "No consecutive numbers appear.")
TestCase().assertEqual(is_shuffled_well([1, 3, 5, 7, 9, 2, 4, 6, 8, 10]), True, "No consecutive numbers appear.")
TestCase().assertEqual(is_shuffled_well([5, 6, 7, 9, 1, 10, 3, 8, 2, 4]), False)
TestCase().assertEqual(is_shuffled_well([3, 9, 7, 5, 2, 4, 10, 1, 8, 6]), True)
TestCase().assertEqual(is_shuffled_well([6, 4, 2, 1, 3, 7, 8, 10, 5, 9]), True)
TestCase().assertEqual(is_shuffled_well([2, 6, 10, 9, 8, 1, 4, 7, 3, 5]), False)
TestCase().assertEqual(is_shuffled_well([6, 10, 5, 8, 4, 2, 7, 9, 3, 1]), True)
TestCase().assertEqual(is_shuffled_well([3, 10, 5, 2, 6, 9, 8, 4, 1, 7]), True)
TestCase().assertEqual(is_shuffled_well([10, 7, 9, 5, 4, 6, 3, 8, 2, 1]), True)
TestCase().assertEqual(is_shuffled_well([3, 5, 9, 6, 10, 1, 4, 8, 7, 2]), True)
TestCase().assertEqual(is_shuffled_well([10, 7, 8, 4, 3, 9, 5, 1, 2, 6]), True)
TestCase().assertEqual(is_shuffled_well([2, 4, 8, 7, 3, 9, 1, 10, 6, 5]), True)
TestCase().assertEqual(is_shuffled_well([9, 6, 1, 3, 10, 8, 5, 4, 7, 2]), True)
TestCase().assertEqual(is_shuffled_well([2, 3, 9, 7, 10, 8, 4, 6, 1, 5]), True)
TestCase().assertEqual(is_shuffled_well([3, 8, 5, 6, 2, 7, 4, 1, 10, 9]), True)
TestCase().assertEqual(is_shuffled_well([1, 6, 4, 10, 3, 5, 7, 2, 9, 8]), True)
TestCase().assertEqual(is_shuffled_well([1, 10, 8, 9, 2, 3, 4, 7, 5, 6]), False)
TestCase().assertEqual(is_shuffled_well([5, 4, 3, 10, 9, 2, 7, 6, 8, 1]), False)
TestCase().assertEqual(is_shuffled_well([4, 7, 8, 3, 5, 9, 2, 6, 1, 10]), True)
TestCase().assertEqual(is_shuffled_well([5, 8, 6, 7, 3, 2, 4, 9, 10, 1]), True)
TestCase().assertEqual(is_shuffled_well([3, 7, 1, 4, 8, 6, 5, 9, 10, 2]), True)
TestCase().assertEqual(is_shuffled_well([10, 1, 9, 4, 3, 2, 7, 8, 6, 5]), False)
TestCase().assertEqual(is_shuffled_well([3, 2, 6, 4, 1, 5, 8, 10, 9, 7]), True)
TestCase().assertEqual(is_shuffled_well([1, 7, 8, 5, 9, 10, 4, 6, 2, 3]), True)
TestCase().assertEqual(is_shuffled_well([2, 3, 9, 7, 5, 6, 8, 1, 10, 4]), True)
TestCase().assertEqual(is_shuffled_well([1, 9, 3, 4, 6, 2, 10, 8, 7, 5]), True)
TestCase().assertEqual(is_shuffled_well([1, 7, 8, 5, 10, 9, 6, 4, 2, 3]), True)
TestCase().assertEqual(is_shuffled_well([2, 9, 10, 3, 5, 7, 6, 4, 8, 1]), True)
TestCase().assertEqual(is_shuffled_well([6, 3, 10, 8, 5, 2, 1, 9, 7, 4]), True)
TestCase().assertEqual(is_shuffled_well([6, 8, 7, 3, 4, 9, 5, 10, 1, 2]), True)
TestCase().assertEqual(is_shuffled_well([8, 4, 9, 5, 6, 3, 1, 10, 7, 2]), True)
