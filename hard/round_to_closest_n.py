def round_number(num, n):
    for number in range(num + (n // 2), -1, -1):
        if number % n == 0:
            return number


print(round_number(33, 25))
