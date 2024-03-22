"""
Recursion: Modulo by Subtraction

The modulo operation can also be done by repetitive subtraction or addition.
In this challenge, you're going to create a function that mimics such
an operation and returns the modulo of the two given numbers by recursively subtracting or adding them.

Examples
modulo(100, 25) ➞ 0

modulo(-51, -4) ➞ -3

modulo(3, 9) ➞ 3

modulo(-21, 5) ➞ -1
# -1 instead of 4 (which is what actually Python
# yields with the modulo operator %)

modulo(1024, 7) ➞ 2

modulo(273, -6) ➞ 3
Notes
There will be no zero-values for the modulo divisor.
You're expected to solve this challenge using a recursive approach.


"""

from unittest import TestCase


def modulo(dividend, divisor):
    if abs(dividend) < abs(divisor):
        return dividend
    elif dividend < 0 and divisor < 0:
        return modulo(dividend + abs(divisor), divisor)
    elif dividend < 0 < divisor:
        return modulo(dividend + divisor, divisor)
    return modulo(dividend - abs(divisor), divisor)


num_vector, res_vector = [[100, 25], [-51, -4], [3, 9], [-21, 5], [1024, 7], [273, -6]], [0, -3, 3, -1, 2, 3]

for i, x in enumerate(num_vector):
    TestCase().assertEqual(modulo(*x), res_vector[i])
    print(x)
