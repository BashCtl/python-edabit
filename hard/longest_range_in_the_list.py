"""
Longest Range in the List (Casual Version)


Given a list of integers, find the length of the longest range of consecutive integers that are contained in the sorted version of the list.

Here's an illustrative example. Consider the list:

[4, 9, 10, 5, 17, 3, 8, 11, 1, 12, 18, 20]
... which, after sorting, becomes:

[1, 3, 4, 5, 8, 9, 10, 11, 12, 17, 18, 20]
The longest consecutive subsequence is now clearly [8, 9, 10, 11, 12], which has length 5.

Examples
max_consec([4, 9, 10, 5, 17, 3, 8, 11, 1, 12, 18, 20]) ➞ 5
# After sorting list becomes [1, 2, 4, 5, 8, 9, 10, 11, 12, 17, 18, 20]
# Longest consecutive subsequence is [8, 9, 10, 11, 12], which has length 5

max_consec([14, 13, 7, 1, 4, 12, 3, 7, 7, 12, 11, 5, 7]) ➞ 4
# After sorting get [1, 3, 4, 5, 7, 7, 7, 7, 11, 12, 12, 13, 14]
# Longest consecutive subsequence is [11, 12, 13, 14], which has length 4

max_consec([13, 3, 8, 5, 5, 2, 13, 6, 14, 2, 11, 4, 10, 8, 1, 9]) ➞ 6
# After sorting get [1, 2, 2, 3, 4, 5, 5, 6, 8, 8, 9, 10, 11, 13, 13, 14]
# Longest consecutive subsequence is [1, 2, 3, 4, 5, 6], which has length 6
Notes
As in the 2nd and 3rd examples, the given list is allowed to include repeated elements, but such repetitions are ignored when finding the longest range of consecutive elements.



"""


from unittest import TestCase


def max_consec(lst):
    slist = sorted(set(lst))
    length = len(slist)
    count = 1
    result = 1

    for i in range(1, length):
        if slist[i] == slist[i - 1] + 1:
            count += 1
        else:
            result = max(result, count)
            count = 1
    result = max(result, count)

    return result


TestCase().assertEqual(max_consec([4, 9, 10, 5, 17, 3, 8, 11, 1, 12, 18, 20]), 5)
TestCase().assertEqual(max_consec([14, 13, 7, 1, 4, 12, 3, 7, 7, 12, 11, 5, 7]), 4)
TestCase().assertEqual(max_consec([13, 3, 8, 5, 5, 2, 1, 13, 8, 6, 14, 2, 11, 4, 10, 8, 1, 10, 9]), 6)
TestCase().assertEqual(max_consec([1, 4, 14, 9, 7, 9, 3, 13, 7, 4, 14, 11, 14, 8, 1, 11, 0, 1]), 3)
TestCase().assertEqual(max_consec([2, 3, 7, 2, 14, 4, 7, 3, 10, 2, 8, 7, 14, 9, 5, 7, 3]), 4)
TestCase().assertEqual(
    max_consec([1, 1, 14, 8, 11, 13, 0, 3, 9, 6, 11, 4, 10, 12, 5, 2, 13, 13, 10, 3, 7, 12, 14, 0, 0, 10, 6, 12]), 15)
TestCase().assertEqual(max_consec([11, 10, 13, 6, 10, 14, 4, 0, 12, 9, 13, 2, 3, 13, 4, 3, 10]), 6)
