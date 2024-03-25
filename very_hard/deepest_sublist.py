"""
Deepest Sublist

You are given a list which may contain sublists.
Your task is to find the depth of the deepest sublist.

[a] = 1 depth
[[a]] = 2 depth
[[[a]]] = 3 depth, etc
Examples
deepest([1, [2, 3], 4, [5, 6]]) ➞ 2

deepest([[[[[[[[[[1]]]]]]]]]]) ➞ 10

deepest([1, 4, [1, 4, [1, 4, [1, 4, [5

"""


def deepest(lst):
    if not isinstance(lst, list):
        return 0
    return 1 + max((deepest(item) for item in lst), default=0)


from unittest import TestCase

TestCase().assertEqual(deepest([1, 4, 5]), 1)
TestCase().assertEqual(deepest([[2, 3], 4, [6, 7, [8]]]), 3)
TestCase().assertEqual(deepest([5, [[[[[[[[[[2]]]]]]]]]], [[[[[[[[[[[[4]]]]]]]]]]]]]), 13)
TestCase().assertEqual(deepest([[[3, 2, [[4]], 8], [[2, 4], 5]], 3, 5, [9, 1]]), 5)
TestCase().assertEqual(deepest([[6, 9, 6], [[[1, 4], 0, 8], [8, 0, [4, 1]]], [[5, 3, 4], [4, 3, 5]]]), 4)
