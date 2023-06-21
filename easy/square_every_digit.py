def square_digits(n):
    ls = [int(x) * int(x) for x in str(n)]
    return int("".join(map(str, ls)))


print(square_digits(9119))
