import re


def is_odd(n):
    return n & 1 == 1


def is_even(n):
    return True if re.match("^-?\\d*[02468]$", n) else False


print(is_odd(5))
print(is_odd(6))

print(is_even("0"))