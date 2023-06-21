def reverse(arg):
    if isinstance(arg, bool):
        return not arg
    return "boolean expected"


print(reverse(True))
print(reverse(0))
