def simon_says(lst1, lst2):
    return lst1[:-1] == lst2[1:]


print(simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]))
print(simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]))