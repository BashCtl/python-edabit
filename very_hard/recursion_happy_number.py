def is_happy(n):
    if n == 4:
        return False
    if n == 1:
        return True
    n = sum([int(d) * int(d) for d in str(n)])
    return is_happy(n)


print(is_happy(67))
print(is_happy(89))
print(is_happy(139))