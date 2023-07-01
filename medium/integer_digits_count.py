def count(n):
    if 10 > n > -10:
        return 1
    return 1 + count(n / 10)


print(count(318))
print(count(-92563))
print(count(4666))
print(count(-314890))
