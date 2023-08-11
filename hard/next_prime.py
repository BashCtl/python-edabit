def next_prime(num):
    while True:
        if is_prime(num):
            return num
        num += 1


def is_prime(num):
    for x in range(2, num // 2):
        if num % x == 0:
            return False
    return True


print(next_prime(12))
print(next_prime(24))
print(next_prime(11))
