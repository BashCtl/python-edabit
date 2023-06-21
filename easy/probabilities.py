def probability(lst, n):
    f = list(filter(lambda x: x >= n, lst))
    return round((len(f) / len(lst)) * 100, 1)


print(probability([5, 1, 8, 9], 6))
print(probability([7, 4, 17, 14, 12, 3], 16))
