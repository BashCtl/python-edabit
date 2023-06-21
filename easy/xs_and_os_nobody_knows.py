def XO(txt):
    txt = txt.lower()
    return txt.count("o") == txt.count("x")


print(XO("ooxx"))
print(XO("xooxx"))
print(XO("ooxXm"))
print(XO("zzoo"))
