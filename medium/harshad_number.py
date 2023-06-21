def is_harshad(n):
    return n % sum([int(v) for v in str(n)]) == 0


print(is_harshad(75))
print(is_harshad(171))
print(is_harshad(481))