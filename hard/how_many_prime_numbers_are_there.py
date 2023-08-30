def prime_numbers(num):
    return len([n for n in range(2, num + 1) if is_prime(n)])


def is_prime(n):
    for i in range(2, (n // 2) + 1):
        if n % i == 0:
            return False
    return True


print(prime_numbers(10))
print(prime_numbers(20))
print(prime_numbers(30))
