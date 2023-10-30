"""
Sieve of Eratosthenes

Given num as input, return a list with all primes up to num included.

Examples
eratosthenes(1) ➞ []

eratosthenes(10) ➞ [2, 3, 5, 7]

eratosthenes(20) ➞ [2, 3, 5, 7, 11, 13, 17, 19]

eratosthenes(0) ➞ []


"""


def eratosthenes(num):
    prime = [True for _ in range(num + 1)]
    i = 2
    while i * i <= num:
        if prime[i]:
            for x in range(i * i, num + 1, i):
                prime[x] = False
        i += 1

    return [p for p in range(2, num + 1) if prime[p]]


print(eratosthenes(1))
print(eratosthenes(10))
print(eratosthenes(20))