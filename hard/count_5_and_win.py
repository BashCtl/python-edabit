"""
Count 5s and Win.

Arun is obsessed with primes, especially five.
He considers a number to be luckiest if it has the highest number of five in it.
If two numbers have the same frequency of five,
Arun considers the larger of them to be luckiest, and if there is no five in any number,
the first given number is considered luckiest. Help him choose the luckiest number.

Examples
get_luckiest([5, 12, 55, 11]) ➞ 55

get_luckiest([5, 12, -55,  11]) ➞ -55

get_luckiest([515, 1255, -55,  1]) ➞ 1255

get_luckiest([44, 12, 7, 40]) ➞ 44
Notes
Return None if given an empty list.

"""

from unittest import TestCase


def get_luckiest(list_of_numbers):
    if list_of_numbers:
        numbers = sorted(list_of_numbers, key=lambda x: (str(x).count('5'), x))
        return numbers[-1] if "5" in str(numbers[-1]) else list_of_numbers[0]
    return None


TestCase().assertEqual(get_luckiest([]), None)
TestCase().assertEqual(get_luckiest([-55, -155, 45, 31, 67]), -55)
TestCase().assertEqual(get_luckiest([5, 12, 55, 11]), 55)
TestCase().assertEqual(get_luckiest([5, 12, -55, 11]), -55)
TestCase().assertEqual(get_luckiest([515, 1255, -55, 1]), 1255)
TestCase().assertEqual(get_luckiest([44, 12, 7, 40]), 44)
TestCase().assertEqual(get_luckiest([-1, -43, -67, 3]), -1)
