"""
Sum of Digits

Create a function that takes a range of numbers
and returns the sum of each digit from start to stop.

Examples
digits_sum(1, 10) ➞ 46
# total numbers in the range are = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# sum of each digits is = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 1 + 0 = 46

digits_sum(1, 20) ➞ 102

digits_sum(1, 100) ➞ 901
Notes
start and stop are inclusive in the range.
"""


def digits_sum(start, stop):
    if stop - start <= 10:
        return sum(int(digit) for number in range(start, stop + 1) for digit in str(number))
    else:
        mid = (start + stop) // 2
        return digits_sum(start, mid) + digits_sum(mid + 1, stop)




from unittest import TestCase

TestCase().assertEqual(digits_sum(1, 5), 15)
TestCase().assertEqual(digits_sum(2, 8), 35)
TestCase().assertEqual(digits_sum(5, 12), 41)
TestCase().assertEqual(digits_sum(1, 10), 46)
TestCase().assertEqual(digits_sum(1, 20), 102)
TestCase().assertEqual(digits_sum(1, 100), 901)
TestCase().assertEqual(digits_sum(14, 112), 909)
TestCase().assertEqual(digits_sum(3, 1000), 13498)
TestCase().assertEqual(digits_sum(1, 10000000), 315000001)
TestCase().assertEqual(digits_sum(1, 100000000), 3600000001)
