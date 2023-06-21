import math


def cars_needed(n):
    return 1 if 0 < n <= 5 else n // 5 + (1 if n % 5 > 0 else 0)


print(cars_needed(5))
print(cars_needed(11))
print(cars_needed(0))
print(cars_needed(8))
