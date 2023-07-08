def match_last_item(lst):
    return "".join([str(i) if type(i) != str else i for i in lst[:-1]]) == lst[-1]


print(match_last_item(["rsq", "6hi", "g", "rsq6hig"]))
print(match_last_item([1, 1, 1, "11"]))
print(match_last_item([8, "thunder", True, "8thunderTrue"]))
