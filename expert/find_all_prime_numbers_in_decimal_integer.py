"""
Find All Prime Numbers in Decimal Integer

Create a function that takes an integer argument and returns
a list of prime numbers found in the decimal representation of that number (not factors).

For example, extract_primes(1717) returns [7, 7, 17, 17, 71].

The list should be in ascending order. If a prime number appears more than once,
every occurrence should be listed. If no prime numbers are found, return an empty list.

Examples
extract_primes(1) ➞ []

extract_primes(7) ➞ [7]

extract_primes(73) ➞ [3, 7, 73]

extract_primes(103) ➞ [3]

extract_primes(1313) ➞ [3, 3, 13, 13, 31, 131, 313]

Notes
All test cases are positive real integers.
Some numbers will have leading zeros. For example, the number 103 contains the
prime number 3, but also contains 03. These should be treated as the same number,
so the result would simply be [3].

"""


def get_digits(num):
    numbers = []
    num = str(num)
    for i in range(len(num)):
        for j in range(i, len(num)):
            numbers.append(num[i:j + 1])
    result =[]
    for n in numbers:
        if n.startswith("0") and n.lstrip("0") in numbers:
            continue
        else:
            result.append(int(n))

    return result


def is_prime(num):
    if num <= 1:
        return False
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


def extract_primes(num):
    numbers = get_digits(num)
    return sorted([n for n in numbers if is_prime(n)])


print(extract_primes(1))
print(extract_primes(2))
print(extract_primes(3))
print(extract_primes(13))
print(extract_primes(101))
print(extract_primes(313))
print(extract_primes(10234))
