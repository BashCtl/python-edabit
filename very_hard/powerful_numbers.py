"""
Powerful Numbers

Given a positive number x:

p = (p1, p2, …)
# Set of *prime* factors of x
If the square of every item in p is also a factor of x, then x is said to be a powerful number.

Create a function that takes a number and returns True if it's powerful, False if it's not.

Examples
is_powerful(36) ➞ True
# p = (2, 3) (prime factors of 36)
# 2^2 = 4 (factor of 36)
# 3^2 = 9 (factor of 36)

is_powerful(27) ➞ True

is_powerful(674) ➞ False

"""
from unittest import TestCase
def is_powerful(n):
    def prime_factors(n):
        factors = set()
        # Check for number of 2s
        while n % 2 == 0:
            factors.add(2)
            n //= 2
        # Check for odd factors from 3 onwards
        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                factors.add(i)
                n //= i
        # If n becomes a prime number greater than 2
        if n > 2:
            factors.add(n)
        return factors

    primes = prime_factors(n)
    for p in primes:
        if n % (p * p) != 0:
            return False
    return True


TestCase().assertEqual(is_powerful(36), True)
TestCase().assertEqual(is_powerful(27), True)
TestCase().assertEqual(is_powerful(32), True)
TestCase().assertEqual(is_powerful(72), True)
TestCase().assertEqual(is_powerful(243), True)
TestCase().assertEqual(is_powerful(968), True)
TestCase().assertEqual(is_powerful(951), False)
TestCase().assertEqual(is_powerful(144), True)
TestCase().assertEqual(is_powerful(674), False)
TestCase().assertEqual(is_powerful(600), False)
TestCase().assertEqual(is_powerful(500), True)
TestCase().assertEqual(is_powerful(320), False)
TestCase().assertEqual(is_powerful(720), False)