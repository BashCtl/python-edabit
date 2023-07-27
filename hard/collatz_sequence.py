def max_collatz(num):
    result = [num]
    while num != 1:
        if num % 2 == 0:
            num //= 2
            result.append(num)
        else:
            num = num * 3 + 1
            result.append(num)

    return max(result)


print(max_collatz(10))
