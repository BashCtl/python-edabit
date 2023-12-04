from unittest import TestCase

"""
Truncatable Primes

A left-truncatable prime is a prime number that contains no 0 digits and, 
when the first digit is successively removed, the result is always prime.

A right-truncatable prime is a prime number that contains no 0 digits and, 
when the last digit is successively removed, the result is always prime.

Create a function that takes an integer as an argument and:

If the integer is only a left-truncatable prime, return "left".
If the integer is only a right-truncatable prime, return "right".
If the integer is both, return "both".
Otherwise, return False.

Examples
truncatable(9137) ➞ "left"
# Because 9137, 137, 37 and 7 are all prime.

truncatable(5939) ➞ "right"
# Because 5939, 593, 59 and 5 are all prime.

truncatable(317) ➞ "both"
# Because 317, 17 and 7 are all prime and 317, 31 and 3 are all prime.

truncatable(5) ➞ "both"
# The trivial case of single-digit primes is treated as truncatable from both directions.

truncatable(139) ➞ False
# 1 and 9 are non-prime, so 139 cannot be truncatable from either direction.

truncatable(103) ➞ False
# Because it contains a 0 digit (even though 103 and 3 are primes).
Notes
The input integers will not exceed 10^6.

"""


def is_prime(num):
    if num <= 1:
        return False
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


def left_prime(num):
    while len(num) != 0:
        if not is_prime(int(num)):
            return False
        num = num[1:]
    return True


def right_prime(num):
    while len(num) != 0:
        if not is_prime(int(num)):
            return False
        num = num[:-1]
    return True


def truncatable(n):
    num = str(n)
    if '0' not in num and is_prime(n):
        left_num = num[1:]
        right_num = num[:-1]
        is_left = left_prime(left_num)
        is_right = right_prime(right_num)
        if is_left and is_right:
            return 'both'
        elif is_right:
            return 'right'
        elif is_left:
            return 'left'

    return False




TestCase().assertEqual(truncatable(47), "left")
TestCase().assertEqual(truncatable(347), "left")
TestCase().assertEqual(truncatable(62383), "left")
TestCase().assertEqual(truncatable(79), "right")
TestCase().assertEqual(truncatable(7331), "right")
TestCase().assertEqual(truncatable(233993), "right")
TestCase().assertEqual(truncatable(3797), "both")
TestCase().assertEqual(truncatable(739397), "both")
TestCase().assertEqual(truncatable(5), "both", "single-digit number treated as both")
TestCase().assertEqual(truncatable(349), False)
TestCase().assertEqual(truncatable(2317), False, "the starting number is composite")
TestCase().assertEqual(truncatable(131), False, "1 is not a prime")
TestCase().assertEqual(truncatable(6043), False, "cannot contain a 0 digit")
