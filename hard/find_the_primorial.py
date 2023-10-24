import numpy


def primorial(n):
    result = []
    count = 0
    start = 2
    while count != n:
        if is_prime(start):
            count += 1
            result.append(start)
        start += 1
    return numpy.prod(result)


def is_prime(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


# print(primorial(1))
# print(primorial(2))
print(primorial(3))
# print(primorial(8))
