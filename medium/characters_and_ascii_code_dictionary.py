def to_dict(lst):
    return [{k: ord(k)} for k in lst]


print(to_dict(["a", "b", "c"]))
