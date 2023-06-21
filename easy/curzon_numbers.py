def is_curzon(num):
    n1 = 2 ** num + 1
    n2 = 2 * num + 1
    return n1 % n2 == 0


print(is_curzon(5))
print(is_curzon(10))
