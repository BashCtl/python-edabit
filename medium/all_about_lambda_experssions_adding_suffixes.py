def add_suffix(suffix):
    return lambda a: a + suffix


add_ly = add_suffix("ly")
print(add_ly("hopeless"))
