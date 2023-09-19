def sorting(s):
    return "".join(sorted(s, key=lambda a: (a.isdigit(),a.lower(), a.isupper())))


print(sorting("eA2a1E"))
print(sorting("Re4r"))
print(sorting("6jnM31Q"))
print(sorting("846ZIbo"))