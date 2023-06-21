def is_isogram(txt):
    txt = txt.lower()
    return len(set(txt)) == len(txt)


print(is_isogram("Algorism"))
print(is_isogram("PasSword"))
