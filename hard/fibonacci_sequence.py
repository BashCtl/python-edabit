def fibo(n):
    fibs = [1, 1]
    for i in range(1, n):
        fibs.append(fibs[i] + fibs[i - 1])
    return fibs[n-1]


print(fibo(1))
print(fibo(2))
print(fibo(3))
print(fibo(6))
