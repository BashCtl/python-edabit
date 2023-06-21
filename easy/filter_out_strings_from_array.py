def filter_list(lst):
    return [x for x in lst if isinstance(x, int)]


print(filter_list([1, 2, "a", "b"]))
print(filter_list([1, 2, "aasf", "1", "123", 123]))
