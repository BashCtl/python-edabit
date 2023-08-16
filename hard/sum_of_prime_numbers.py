def sum_primes(lst):
    return sum(list(filter(is_prime, lst))) if len(lst) > 0 else None


def is_prime(num):
    for x in range(2, (num // 2) + 1):
        if num % x == 0:
            return False
    return True if num > 1 else False


print(sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sum_primes([2, 3, 4, 11, 20, 50, 71]))
print(sum_primes([]))
