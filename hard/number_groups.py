def number_groups(group1, group2, group3):
    s1 = list(set(group1).intersection(set(group2)))
    s2 = list(set(group1).intersection(set(group3)))
    s3 = list(set(group2).intersection(set(group3)))
    return sorted(list(set(s1+s2+s3)))


print(number_groups([7, 8, 7, 3, 4], [2, 9, 1, 2, 1], [5, 6, 6, 6, 5]))
print(number_groups([3, 8, 8, 1, 1], [9, 1, 1, 9, 9], [10, 7, 6, 6, 3]))
