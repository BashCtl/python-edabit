def digits_count(n):
    if -10 < n < 10:
        return 1
    return 1 + digits_count(n // 10)


print(digits_count(4666))
print(digits_count(-1232323))
print(digits_count(3463463874638476))
