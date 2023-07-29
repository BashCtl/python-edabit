def letters(word1, word2):
    s1 = set(word1)
    s2 = set(word2)
    common = "".join(sorted(s1.intersection(s2)))
    diff1 = "".join(sorted(s1.difference(s2)))
    diff2 = "".join(sorted(s2.difference(s1)))
    return [common, diff1, diff2]


print(letters("sharp", "soap"))
