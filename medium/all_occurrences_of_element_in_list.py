def get_indices(lst, el):
    return [i for i, e in enumerate(lst) if lst[i] == el]


print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))
print(get_indices([1, 5, 5, 2, 7], 8))