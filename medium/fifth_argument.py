def fifth(*args):
    return type(list(args)[4]) if len(args) >= 5 else "Not enough arguments"


print(fifth(1, 2, 3, 4, 5))
print(fifth("a", 2, 3, [1, 2, 3], "five"))
print(fifth())