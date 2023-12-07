"""
The Kempner Function

The Kempner Function, applied to a composite number, permits to find the smallest integer greater than zero whose factorial is exactly divided by the number.

kempner(6) ➞ 3

1! = 1 % 6 > 0
2! = 2 % 6 > 0
3! = 6 % 6 === 0

kempner(10) ➞ 5

1! = 1 % 10 > 0
2! = 2 % 10 > 0
3! = 6 % 10 > 0
4! = 24 % 10 > 0
5! = 120 % 10 === 0
A Kempner Function applied to a prime will always return the prime itself.

kempner(2) ➞ 2
kempner(5) ➞ 5
Given an integer n, implement a Kempner Function.

Examples
kempner(6) ➞ 3

kempner(10) ➞ 5

"""

def factorial(num):
    if num == 1:
        return num
    return num * factorial(num - 1)


def kempner(n, x=1):
    fact = factorial(x)
    if fact % n == 0:
        return x
    return kempner(n, x + 1)


print(kempner(6))
print(kempner(10))
