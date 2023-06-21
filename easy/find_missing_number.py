def missing_num(lst):
    return sum(range(1, 11)) - sum(lst)


print(missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]))
