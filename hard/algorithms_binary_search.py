def is_prime(primes, num, left=0, right=None):
    right = len(primes) - 1
    while left <= right:
        mid = (left + right) // 2
        if primes[mid] == num:
            return "yes"
        elif primes[mid] < num:
            left = mid + 1
        else:
            right = mid - 1
    return "no"
