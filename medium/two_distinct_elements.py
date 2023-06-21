def return_unique(lst):
    return [x for x in lst if lst.count(x) == 1]


print(return_unique([9, 5, 6, 8, 7, 7, 1, 1, 1, 1, 1, 9, 8]))