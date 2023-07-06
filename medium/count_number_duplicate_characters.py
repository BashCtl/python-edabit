def duplicates(txt):
    return sum([txt.count(l)-1 if txt.count(l)>1 else 0 for l in set(txt)])


print(duplicates("Hello World!"))