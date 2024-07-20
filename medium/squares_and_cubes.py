"""
Squares and Cubes
Create a function that takes a list of two numbers and checks if the square root of the first number is equal to the cube root of the second number.

Examples
check_square_and_cube([4, 8]) ➞ True

check_square_and_cube([16, 48]) ➞ False

check_square_and_cube([9, 27]) ➞ True
Notes
Remember to return either True or False.
All lists contain two positive numbers.

"""

from unittest import TestCase


def check_square_and_cube(lst):
    num1, num2 = lst
    sqrt_num1 = num1 ** 0.5
    cbrt_num2 = num2 ** (1 / 3)

    return abs(sqrt_num1 - cbrt_num2) < 1e-9


TestCase().assertEqual(check_square_and_cube([4, 8]), True)
TestCase().assertEqual(check_square_and_cube([5, 12]), False)
TestCase().assertEqual(check_square_and_cube([9, 27]), True)
TestCase().assertEqual(check_square_and_cube([25, 120]), False)
TestCase().assertEqual(check_square_and_cube([25, 125]), True)
TestCase().assertEqual(check_square_and_cube([36, 215]), False)
TestCase().assertEqual(check_square_and_cube([36, 217]), False)
TestCase().assertEqual(check_square_and_cube([144, 1728]), True)
TestCase().assertEqual(check_square_and_cube([1, 1]), True)
TestCase().assertEqual(check_square_and_cube([676, 17576]), True)
