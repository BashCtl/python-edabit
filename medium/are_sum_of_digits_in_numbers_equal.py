def is_equal(lst):
    result = [sum([int(x) for x in str(item)]) for item in lst]
    return result[0] == result[1]


print(is_equal([105, 42]))
print(is_equal([21, 35]))
print(is_equal([0,0]))
