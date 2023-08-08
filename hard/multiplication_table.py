def multiplication_table(n):
    return [[i for i in range(x, x * n+1,x)] for x in range(1, n + 1)]


print(multiplication_table(3))
