def can_build(s1, s2):
    return all([s1.count(l) >= s2.count(l) for l in s2])


print(can_build("aPPleAL", "PAL"))
print(can_build("aPPleAL", "apple"))