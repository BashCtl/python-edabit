"""
Three Sum Problem


Write a function that returns all sets of three elements that sum to 0.

Examples
three_sum([0, 1, -1, -1, 2]) ➞ [[0, 1, -1], [-1, -1, 2]]

three_sum([0, 0, 0, 5, -5]) ➞ [[0, 0, 0], [0, 5, -5]]

three_sum([1, 2, 3]) ➞ []

three_sum([1]) ➞ []
Notes
The original list may contain duplicate numbers.
Each three-element sublist in your output should be distinct.
Sublists should be ordered by the first element of the sublist.
Sublists themselves should be ordered the same as the original list.
Return an empty list if no three elements sum to zero.
Return an empty list if there are fewer than three elements.

"""
from unittest import TestCase


def three_sum(lst):
    result = []

    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j + 1, len(lst)):
                temp = [lst[i], lst[j], lst[k]]
                if sum(temp) == 0:
                    if temp not in result:
                        result.append(temp)

    return result


TestCase().assertEqual(three_sum([0, 1, -1, -1, 2]), [[0, 1, -1], [-1, -1, 2]])
TestCase().assertEqual(three_sum([0, 0, 0, 5, -5]), [[0, 0, 0], [0, 5, -5]])
TestCase().assertEqual(three_sum([0, -1, 1, 0, -1, 1]), [[0, -1, 1], [0, 1, -1], [-1, 1, 0], [-1, 0, 1], [1, 0, -1]])
TestCase().assertEqual(three_sum([0, 5, 5, 0, 0]), [[0, 0, 0]])
TestCase().assertEqual(three_sum([0, 5, -5, 0, 0]), [[0, 5, -5], [0, 0, 0], [5, -5, 0]])
TestCase().assertEqual(three_sum([1, 2, 3, -5, 8, 9, -9, 0]), [[1, 8, -9], [2, 3, -5], [9, -9, 0]])
TestCase().assertEqual(three_sum([0, 0, 0]), [[0, 0, 0]])
TestCase().assertEqual(three_sum([1, 5, 5, 2]), [])
TestCase().assertEqual(three_sum([1, 1]), [])
TestCase().assertEqual(three_sum([]), [])
