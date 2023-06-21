def number_length(num):
    if num // 10 == 0:
        return 1
    return 1 + number_length(num // 10)


print(number_length(10))
print(number_length(5000))
print(number_length(0))