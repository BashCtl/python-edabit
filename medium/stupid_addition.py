def stupid_addition(a, b):
    if type(a) == int and type(b) == int:
        return str(a) + str(b)
    elif type(a) == str and type(b) == str:
        return int(a) + int(b)
    return None


print(stupid_addition(1,2))
print(stupid_addition("1", "2"))
print(stupid_addition("1", 2))