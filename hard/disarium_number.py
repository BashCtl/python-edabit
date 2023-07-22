def is_disarium(n):
    return sum([int(number) ** (i + 1) for i, number in enumerate(str(n))]) == n


print(is_disarium(75))
print(is_disarium(135))
