"""
Count the Primes within a Range

Given two integers create a function that counts the number of primes between the two given integers.

Examples
prime_count(1, 10) ➞ 4
# range = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# primes = [2, 3, 5, 7]
# answer = 4

prime_count(1, 100) ➞ 25

prime_count(1, 1000) ➞ 168
Notes
If there are no primes within the given range, return 0.


"""


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def prime_count(a, b):
    count = 0
    for number in range(a, b + 1):
        if is_prime(number):
            count += 1

    return count


print(prime_count(1, 1000))
