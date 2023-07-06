def neutralise(s1, s2):
    return "".join([x if y == x else "0" for x, y in zip(s1, s2)])


print(neutralise("+-+", "+--"))
print(neutralise("-+-+-+", "-+-+-+"))
print(neutralise("--++--", "++--++"))
