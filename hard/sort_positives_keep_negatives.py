def pos_neg_sort(lst):
    positive = sorted([i for i in lst if i >= 0])
    j = 0
    for i in range(len(lst)):
        if lst[i] >= 0:
            lst[i] = positive[j]
            j += 1
    return lst


print(pos_neg_sort([6, 3, -2, 5, -8, 2, -2]))
