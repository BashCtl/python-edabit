def collatz(n):
    result = [n]
    while n != 1:
        if n & 1 == 0:
            n //= 2
            result.append(n)
        else:
            n = n * 3 + 1
            result.append(n)
    return [len(result) - 1, max(result)]


print(collatz(17))
print(collatz(6))
print(collatz(21))