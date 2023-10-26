def is_polydivisible(n):
    if str(n)[0] != '0':
        for i in range(1, len(str(n)) + 1):
            if int(str(n)[:i]) % i != 0:
                return False
    return True


print(is_polydivisible(1232))
print(is_polydivisible(123220))
