"""
Moran Numbers

A Harshad number is a number which is divisible by the sum of its digits.
For example, 132 is divisible by 6 (1+3+2).

A subset of the Harshad numbers are the Moran numbers.
Moran numbers yield a prime when divided by the sum of their digits.
For example, 133 divided by 7 (1+3+3) yields 19, a prime.

Create a function that takes a number and returns "M" if the number is a Moran number,
"H" if it is a (non-Moran) Harshad number, or "Neither".

Examples
moran(132) ➞ "H"

moran(133) ➞ "M"

moran(134) ➞ "Neither"
"""


def is_prime(x):
    for i in range(2, (x // 2) + 1):
        if x % i == 0:
            return False
    return True


def moran(n):
    numbers_sum = sum([int(i) for i in str(n)])

    if n % numbers_sum == 0:
        if is_prime(n // numbers_sum):
            return "M"
        else:
            return "H"
    return "Neither"


print(moran(132))
print(moran(133))
print(moran(134))
print(moran(20937))
