def is_subset(lst1, lst2):
    return all(item in lst2 for item in lst1)


print(is_subset([3, 2, 5], [5, 3, 7, 9, 2]))
print(is_subset([8, 9], [7, 1, 9, 8, 4, 5, 6]))
print(is_subset([1, 2], [3, 5, 9, 1]))
