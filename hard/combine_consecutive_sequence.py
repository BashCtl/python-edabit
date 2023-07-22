def consecutive_combo(lst1, lst2):
    lst1.extend(lst2)
    lst1.sort()
    return all([(lst1[i + 1] - lst1[i]) == 1 for i in range(0, len(lst1) - 1)])


print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))
print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))
