def paths(n):
    if n == 1:
        return n
    return n * paths(n - 1)


print(paths(4))
print(paths(9))
