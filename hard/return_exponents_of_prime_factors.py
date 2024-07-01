"""
Return Exponents of Prime Factors

You are given a list of prime factors lst and a target. When each number in the list is raised to an appropriate power their product will be equal to the target.

Your role is to return the exponents. All these lists will have a length of three. Basically, it is three numbers whose product is equal to challenge. The only difference is what you are expected to return.

Examples
product_equal_target([2, 3, 5], 600) ➞ [3, 1, 2]
# Because 2^3*3^1*5^2 = 600

product_equal_target([2, 3, 5], 720) ➞ [4, 2, 1]
# Because 2^4*3^2*5^1 = 720
Notes
The exponents you will return are expected to replace the base in the list.
Your returned values must be in the same order as the bases.

"""


from unittest import TestCase


def product_equal_target(lst, target):
    exponents = []

    for prime in lst:
        count = 0
        while target % prime == 0:
            target //= prime
            count += 1
        exponents.append(count)

    return exponents


TestCase().assertEqual(product_equal_target([2, 3, 5], 720), [4, 2, 1])
TestCase().assertEqual(product_equal_target([2, 3, 19], 1026), [1, 3, 1])
TestCase().assertEqual(product_equal_target([2, 3, 5], 600), [3, 1, 2])
TestCase().assertEqual(product_equal_target([2, 37, 149], 11026),[1, 1, 1])
TestCase().assertEqual(product_equal_target([2, 3, 5], 180), [2, 2, 1])
TestCase().assertEqual(product_equal_target([2, 5, 2711], 54220),[2, 1, 1])