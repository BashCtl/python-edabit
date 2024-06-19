"""
Zipping Up a List



Two lists are part of the same zipper if the ending is identical. The identical section can be thought of as being "zipped-up". Below, [2, 2, 4] is "zipped-up".

List 1: [3, 5, 8, 9, 2, 2, 4]
List 2: [1, 7, 2, 2, 4]
Create a function that takes in two lists. Return False if none of the list is "zipped." Return True if the lists are identical. Otherwise, return a list with the first index in each list where the zipper diverges.

To illustrate:

zipper([3, 5, 8, 9, 2, 2, 4], [1, 7, 2, 2, 4]) ➞ [3, 1]
# Zipper 1: 9 (index-3) is first element to diverge.
# Zipper 2: 7 (index-1) is first element to diverge.
Examples
zipper([5, 5, 7, 8, 9, 1, 2], [3, 2, 1, 1, 6, 6, 6, 6, 1, 2]) ➞ [4, 7]

zipper([5, 4, 3, 2, 6], [6, 4, 3, 2, 6]) ➞ [0, 0]

zipper([5, 4, 3, 2, 7], [6, 4, 3, 2, 6]) ➞ False

zipper([5, 4, 3, 2, 6], [5, 4, 3, 2, 6]) ➞ True
Notes
Use zero-indexing for the lists.

"""

from unittest import TestCase


def zipper(lst1, lst2):
    l1 = len(lst1)
    l2 = len(lst2)
    min_length = min(l1, l2)
    if lst1 == lst2:
        return True
    if lst1[-1] == lst2[-1]:
        for i in range(min_length):
            if lst1[l1 - i - 1] != lst2[l2 - i - 1]:
                return [l1 - i - 1, l2 - i - 1]
    return False


TestCase().assertEqual(zipper([5, 5, 7, 8, 9, 1, 2], [3, 2, 1, 1, 6, 6, 6, 6, 1, 2]), [4, 7])
TestCase().assertEqual(zipper([5, 4, 3, 2, 6], [6, 4, 3, 2, 6]), [0, 0])
TestCase().assertEqual(zipper([5, 4, 3, 2, 7], [6, 4, 3, 2, 6]), False)
TestCase().assertEqual(zipper([1, 5, 4, 3], [9, 8, 7, 5, 4, 3]), [0, 2])
TestCase().assertEqual(zipper([7, 8, 9, 9, 9], [8, 8, 9, 9, 9, 9, 9]), [1, 3])
TestCase().assertEqual(zipper([7, 8, 5, 1, 5], [6, 6, 5, 1, 5]), [1, 1])
TestCase().assertEqual(zipper([6, 6, 5, 1, 5], [6, 6, 5, 1, 5]), True)
TestCase().assertEqual(zipper([1, 1, 2, 6, 6, 5, 1, 5], [7, 8, 9, 4, 4, 6, 6, 5, 1, 5]), [2, 4])
