def to_list(dct):
    return sorted([[k, v] for k, v in dct.items()], key=lambda a: a[0])


print(to_list({}))
print(to_list({"b": 1, "a": 2}))
