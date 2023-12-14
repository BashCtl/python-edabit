from functools import reduce
"""
Least Common Multiple


Given a list of integers, create a function that will find 
the smallest positive integer that is evenly divisible 
by all the members of the list. In other words, 
find the least common multiple (LCM).

Examples
lcm([1, 2, 3, 4, 5, 6, 7, 8, 9]) ➞ 2520

lcm([5]) ➞ 5

lcm([5, 7, 11]) ➞ 385

lcm([5, 7, 11, 35, 55, 77]) ➞ 385

"""


def gcd_two(a, b):
    while b > 0:
        temp = b
        b = a % b
        a = temp

    return a


def lcm(nums):
    return reduce(lambda a, b: a * b // gcd_two(a, b), nums)


print(lcm([5]))
print(lcm([5, 7, 11]))
