def return_only_integer(lst):
    return [d for d in lst if type(d) is int]


print(return_only_integer([9, 2, 3.3, "space", "car", "lion", 16]))