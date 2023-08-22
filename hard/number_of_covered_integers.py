def covered_integers(lst):
    return len(set([i for item in lst for i in range(item[0], item[1] + 1)]))


print(covered_integers([[80, 81], [1, 2], [9, 11]]))
