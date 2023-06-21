def which_is_larger(f, g):
    if f() > g():
        return "f"
    elif g() > f():
        return "g"
    return "neither"


print(which_is_larger(lambda: 5, lambda: 10))
print(which_is_larger(lambda: 15, lambda: 10))
print(which_is_larger(lambda: 15, lambda: 15))
