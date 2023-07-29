import math


def power_ranger(power, minimum, maximum):
    count = 0
    for num in range(1, maximum + 1):
        if minimum <= num ** power <= maximum:
            count += 1
    return count


print(power_ranger(1, 1, 5))

print(power_ranger(2, 49, 65))
print(power_ranger(3, 1, 27))
print(power_ranger(10, 1, 5))
print(power_ranger(5, 31, 33))