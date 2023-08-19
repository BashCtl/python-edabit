def filter_factorials(numbers):
    return list(filter(is_factorial, numbers))


def is_factorial(n):
    i = 1
    fact = 1
    while fact < n:
        i += 1
        fact *= i
    return fact == n


print(filter_factorials([1, 2, 3, 4, 5, 6, 7]))