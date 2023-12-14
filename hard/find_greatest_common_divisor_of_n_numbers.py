from functools import reduce

"""
Find Greatest Common Divisor of N Numbers

Create a function that takes a list of numbers and returns the greatest common factor of those numbers.

Examples
gcd([84, 70, 42, 56]) ➞ 14

gcd([19, 38, 76, 133]) ➞ 19

gcd([120, 300, 95, 425, 625]) ➞ 5

Notes
The GCD is the largest factor that divides all numbers in the list.
"""


def gcd_two(a, b):
    while b > 0:
        temp = b
        b = a % b
        a = temp

    return a


def gcd(lst):
    return reduce(gcd_two, lst)


print(gcd([84, 70, 42, 56]))
