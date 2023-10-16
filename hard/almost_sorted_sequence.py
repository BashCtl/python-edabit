def almost_sorted(lst):
    lst = [l[1] > l[0] for l in zip(lst, lst[1:])]
    return lst.count(True) == 1 or lst.count(False) == 1


print(almost_sorted([1, 3, 5, 9, 11, 80, 15, 33, 37, 41]))
print(almost_sorted([6, 5, 4, 7, 3]))
print(almost_sorted([6, 4, 2, 0]))
print(almost_sorted([7, 8, 9, 3, 10, 11, 12, 2]))
print(almost_sorted([5, 4, 3, 2, -1, 0]))
print(almost_sorted([-3, -4, -5, -7]))
print(almost_sorted([6, 4, 2, 0]))
