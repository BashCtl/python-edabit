def move_to_end(lst, el):
    return [e for e in lst if e != el] + [e for e in lst if e == el]


print(move_to_end([1, 3, 2, 4, 4, 1], 1))
