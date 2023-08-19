def wrap_around(string, offset):
    return (string[(0 + offset) % len(string):]
            + string[:(0 + offset) % len(string)])


print(wrap_around("Hello, World!", 2))
print(wrap_around("Nonscience", -116))
print(wrap_around("Excelsior", 30))
