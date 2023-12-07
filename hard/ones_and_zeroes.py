from unittest import TestCase

import re

"""
Ones and Zeroes

Write a function that returns True if every consecutive sequence of 
ones is followed by a consecutive sequence of zeroes of the same length.

Examples
same_length("110011100010") ➞ True

same_length("101010110") ➞ False

same_length("111100001100") ➞ True

same_length("111") ➞ False
"""


def same_length(txt):
    ones = list(filter(None, re.split("[0]{1,}", txt)))
    zeros = list(filter(None, re.split("1{1,}", txt)))

    return len(ones) == len(zeros) and all(len(one) == len(zero) for one, zero in zip(ones, zeros))


TestCase().assertEqual(same_length('10'), True)
TestCase().assertEqual(same_length('1010'), True)
TestCase().assertEqual(same_length('1100'), True)
TestCase().assertEqual(same_length('10101110001100'), True)
TestCase().assertEqual(same_length('1111000010101100'), True)

TestCase().assertEqual(same_length('1001'), False)
TestCase().assertEqual(same_length('101001'), False)
TestCase().assertEqual(same_length('101'), False)
TestCase().assertEqual(same_length('10010'), False)
TestCase().assertEqual(same_length('110'), False)
TestCase().assertEqual(same_length('11001'), False)
TestCase().assertEqual(same_length('11100011000'), False)
