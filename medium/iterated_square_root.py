import math


def i_sqrt(n):
    count = 0
    if n < 0:
        return "invalid"
    while n >= 2:
        n = math.sqrt(n)
        count += 1
    return count


print(i_sqrt(1))
print(i_sqrt(2))
print(i_sqrt(7))
print(i_sqrt(27))
print(i_sqrt(256))
print(i_sqrt(-1))
