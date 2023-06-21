def is_in_order(txt):
    s = list(txt)
    return sorted(s) == list(txt)


print(is_in_order('abc'))
print(is_in_order('edabit'))
print(is_in_order('123'))
print(is_in_order('xyzz'))
