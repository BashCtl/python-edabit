def count_characters(lst):
    return sum([len(s) for s in lst])


r1 = count_characters([
    "###",
    "###",
    "###"
])
print(r1)
