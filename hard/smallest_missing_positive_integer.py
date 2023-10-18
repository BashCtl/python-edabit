def min_miss_pos(lst):
    lst = sorted(filter(lambda x: x >= 0, lst))
    if len(lst) == 1:
        return lst[0] + 1
    for i in range(len(lst) - 1):
        if lst[i] + 1 != lst[i + 1] and lst[i] != lst[i + 1]:
            return lst[i] + 1
    return lst[-1] + 1


print(min_miss_pos([-2, 6, 4, 5, 7, -1, 1, 3, 6, -2, 9, 10, 2, 2]))
print(min_miss_pos([5, 9, -2, 0, 1, 3, 9, 3, 8, 9]))
print(min_miss_pos([0, 4, 4, -1, 9, 4, 5, 2, 10, 7, 6, 3, 10, 9]))
print(min_miss_pos([0, -4, -4, -1, -9, -4, -5, -2, -10, -7, -6, -3, -10, -9]))
print(min_miss_pos([7, 6, 5, 4, 3, 2, 1]))
