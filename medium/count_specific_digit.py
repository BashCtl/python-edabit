def digit_occurrences(start, end, digit):
    return sum([str(x).count(str(digit)) for x in range(start, end + 1)])


print(digit_occurrences(51, 55, 5))
