def add_indexes(lst):
    return [x + lst[x] for x in range(len(lst))]


print(add_indexes([0, 0, 0, 0, 0]))
print(add_indexes([1, 2, 3, 4, 5]))
