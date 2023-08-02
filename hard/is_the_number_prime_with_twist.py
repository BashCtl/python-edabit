import math


def prime(x):
    if x & 1 == 0:
        return False
    return 2 in [x, pow(2, x, x)]


print(prime(7))
print(prime(5151512515524))
print(prime(777777777777777))
print(prime(100000074281))
