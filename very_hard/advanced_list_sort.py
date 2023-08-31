def advanced_sort(lst):
    # return [[item] * lst.count(item) for item in dict.fromkeys(lst)]
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return [[i] * lst.count(i) for i in unique]


print(advanced_sort([2, 1, 2, 1]))
print(advanced_sort([5, 4, 5, 5, 4, 3]))
print(advanced_sort(["b", "a", "b", "a", "c"]))
print(advanced_sort([1, 2, 1, 2]))
