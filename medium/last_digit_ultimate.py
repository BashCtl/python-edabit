def last_dig(a, b, c):
    return str(int(str(a)[-1]) * int(str(b)[-1]))[-1] == str(c)[-1]


print(last_dig(25, 21, 125))
print(last_dig(55, 226, 5190))
print(last_dig(12, 215, 2142))
