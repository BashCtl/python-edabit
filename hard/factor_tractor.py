"""
Factor Tractor

Write a function to find all the prime factors of a given integer.
The function must return a list containing all the prime factors,
sorted in ascending order. Remember that 1 is neither prime nor composite
and should not be included in your output list.

Examples
prime_factorize(25) ➞ [5, 5]

prime_factorize(19) ➞ [19]

prime_factorize(77) ➞ [7, 11]

Notes

Output list must be sorted in ascending order.
The only positive integer which is neither prime nor composite is 1.
Return an empty list if 1 is the input.

"""


def is_prime(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


def prime_factorize(num, factors=[]):
    f = [n for n in range(2, num + 1) if num % n == 0 and is_prime(n)]
    if f:
        factors.append(f[0])
        return prime_factorize(num // f[0], factors)
    else:
        result = factors.copy()
        factors.clear()
        return result


print(prime_factorize(25))
print(prime_factorize(19))
print(prime_factorize(77))
