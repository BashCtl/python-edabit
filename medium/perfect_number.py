"""
Perfect Number
Create a function that tests whether or not an integer is a perfect number. A perfect number is a number that can be written as the sum of its factors, excluding the number itself.

For example, 6 is a perfect number, since 1 + 2 + 3 = 6, where 1, 2, and 3 are all factors of 6. Similarly, 28 is a perfect number, since 1 + 2 + 4 + 7 + 14 = 28.

Examples
check_perfect(6) ➞ True

check_perfect(28) ➞ True

check_perfect(496) ➞ True

check_perfect(12) ➞ False

check_perfect(97) ➞ False
"""

from unittest import TestCase


def check_perfect(num):
    return sum(x for x in range(1, num) if num % x == 0) == num


TestCase().assertEqual(check_perfect(6), True)
TestCase().assertEqual(check_perfect(28), True)
TestCase().assertEqual(check_perfect(496), True)
TestCase().assertEqual(check_perfect(8128), True)
TestCase().assertEqual(check_perfect(33550336), True)
TestCase().assertEqual(check_perfect(12), False)
TestCase().assertEqual(check_perfect(97), False)
TestCase().assertEqual(check_perfect(481), False)
TestCase().assertEqual(check_perfect(1001), False)
TestCase().assertEqual(check_perfect(55555), False)
