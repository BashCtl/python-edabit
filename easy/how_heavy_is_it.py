import math


def weight(r, h):
    volume = (math.pi * r * r * h) * 0.001
    return round(volume, 2)


print(weight(4, 10))
print(weight(30, 60))
print(weight(15, 10))
