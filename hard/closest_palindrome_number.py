"""
Closest Palindrome Number


Write a function that returns the closest palindrome number to an integer.
If two palindrome numbers tie in absolute distance, return the smaller number.

Examples
closest_palindrome(887) ➞ 888

closest_palindrome(100) ➞ 99
# 99 and 101 are equally distant, so we return the smaller palindrome.

closest_palindrome(888) ➞ 888

closest_palindrome(27) ➞ 22
Notes
If the number itself is a palindrome, return that number.

"""

from unittest import TestCase


def closest_palindrome(num):
    if str(num) == str(num)[::-1]:
        return num
    else:
        lower = num - 1
        upper = num + 1
        while True:

            if str(lower) == str(lower)[::-1]:
                return lower

            if str(upper) == str(upper)[::-1]:
                return upper
            lower -= 1
            upper += 1


TestCase().assertEqual(closest_palindrome(887), 888)
TestCase().assertEqual(closest_palindrome(888), 888)
TestCase().assertEqual(closest_palindrome(27), 22)
TestCase().assertEqual(closest_palindrome(519), 515)
TestCase().assertEqual(closest_palindrome(4892), 4884)
TestCase().assertEqual(closest_palindrome(1), 1)
TestCase().assertEqual(closest_palindrome(100), 99)
TestCase().assertEqual(closest_palindrome(33344), 33333)
TestCase().assertEqual(closest_palindrome(123456), 123321)
TestCase().assertEqual(closest_palindrome(978215236), 978212879)
