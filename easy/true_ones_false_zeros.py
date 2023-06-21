def integer_boolean(n):
    return [bool(int(x)) for x in n]


print(integer_boolean("100101"))