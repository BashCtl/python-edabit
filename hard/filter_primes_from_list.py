def is_prime(num):
    if num == 1:
        return False
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


def filter_primes(num):
    return [n for n in num if is_prime(n)]


print(filter_primes([1, 2, 3, 5, 7, 11, 13, 17, 19, 23]))
