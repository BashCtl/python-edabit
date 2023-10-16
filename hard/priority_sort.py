

def priority_sort(lst, s):
    return sorted(lst, key=lambda i: (i not in s, i))


print(priority_sort([5, 4, 3, 2, 1], {3, 6}))