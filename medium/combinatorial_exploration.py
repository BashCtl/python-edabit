import math


def no_perms_digits(n):
    return len(str(math.factorial(n)))


print(no_perms_digits(0))
print(no_perms_digits(1))
print(no_perms_digits(5))
print(no_perms_digits(8))