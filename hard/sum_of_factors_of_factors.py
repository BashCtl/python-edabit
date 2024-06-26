"""
Sum of Factors of Factors

Create a function that takes a number and returns the sum of factors of factors of the given number.

Examples
sum_ff(69) ➞ 3, 23 ➞ 0
# Both 3 and 23 are prime numbers and have no factors
# other than 1 and themselves so the result is 0.

sum_ff(12) ➞ 2, 3, 4, 6 ➞ (0) + (0) + (2) + (2+3) ➞ 7

sum_ff(420) ➞ 2,4, 6, 10, 12 ... ➞ (2) + (2+3) + (2+5) + (2+3+4+6) ... ➞ 1175

sum_ff(619) ➞ ___ ➞ 0
# 619 doesn't have any factors (other than 1 and 619).
Notes
The number will always be greater than 0.
Factors that are equal to the number or 1, don't count (see example #1).

"""

from unittest import TestCase


def sum_of_factors(n):
    if n <= 1:
        return 0
    factors = [i for i in range(2, n) if n % i == 0]
    return sum(factors)


def sum_ff(n):
    if n <= 1:
        return 0

    factors = [i for i in range(2, n) if n % i == 0]
    total_sum = 0

    for factor in factors:
        total_sum += sum_of_factors(factor)

    return total_sum


TestCase().assertEqual(sum_ff(98), 16)
TestCase().assertEqual(sum_ff(435), 74)
TestCase().assertEqual(sum_ff(534), 188)
TestCase().assertEqual(sum_ff(3123), 353)
TestCase().assertEqual(sum_ff(1232), 1931)
TestCase().assertEqual(sum_ff(12), 7)
TestCase().assertEqual(sum_ff(31232), 32630)
TestCase().assertEqual(sum_ff(4234), 208)
TestCase().assertEqual(sum_ff(655), 0)
TestCase().assertEqual(sum_ff(432), 1240)
TestCase().assertEqual(sum_ff(2343), 170)
