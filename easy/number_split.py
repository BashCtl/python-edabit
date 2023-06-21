import math


def number_split(n):
    num = n / 2
    if n % 2 == 0:
        return [int(num), int(num)]
    else:
        return [math.floor(num), math.ceil(num)]


print(number_split(4))
print(number_split(10))
print(number_split(11))
print(number_split(-9))
