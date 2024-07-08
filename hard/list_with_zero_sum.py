"""
List with Zero Sum

Given an integer n, return any list containing n unique integers such that they add up to 0.

Examples
list_with_zero_sum(5) ➞ [-7, -1, 1, 3, 4] or [-5, -1, 1, 2, 3] or [-3, -1, 2, -2, 4]

list_with_zero_sum(3) ➞ [-1, 0, 1]

list_with_zero_sum(1) ➞ [0]

"""

from unittest import TestCase
from time import perf_counter
from random import randint


def list_with_zero_sum(n):
    result = []
    for i in range(1, n // 2 + 1):
        result.append(i)
        result.append(-i)

    if n % 2 != 0:
        result.append(0)

    return result


tic = perf_counter()

for _ in range(100):
    len_lst = randint(1, 1000)
    output = list_with_zero_sum(len_lst)
    TestCase().assertEqual(len(set(output)) == len_lst and sum(output) == 0, True)

print('t_sec = {:.6f}'.format(perf_counter() - tic))
