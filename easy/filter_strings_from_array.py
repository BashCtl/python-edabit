def filter_list(l):
    return list(filter(lambda n: isinstance(n, int), l))


print(filter_list([1, 2, 3, "a", "b", 4]))
