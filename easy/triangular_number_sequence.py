def triangle(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


print(triangle(215))
