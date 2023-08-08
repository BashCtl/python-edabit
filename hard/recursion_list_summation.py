def recur_add(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + recur_add(lst[1:])


print(recur_add([1, 2, 3, 4, 10, 11]))
