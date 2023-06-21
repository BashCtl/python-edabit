def is_automorphic(n):
    return n == (n ** 2) % (10 ** len(str(n)))


print(is_automorphic(5))
print(is_automorphic(8))
print(is_automorphic(76))
