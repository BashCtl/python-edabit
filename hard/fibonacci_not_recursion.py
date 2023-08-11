def fib(n):
    if 0 < n <= 2:
        return 1
    n1 = 0
    n2 = 1
    result = 0
    for _ in range(n - 1):
        result = n1 + n2
        n1 = n2
        n2 = result
    return result


print(fib(6))
