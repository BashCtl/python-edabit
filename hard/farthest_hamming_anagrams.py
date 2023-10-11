def max_ham(s1, s2):
    ham = 0
    for x, y in zip(s1, s2):
        if x != y:
            ham += 1
    if sorted(s1) == sorted(s2) and ham == len(s1):
        return True
    elif sorted(s1) != sorted(s2):
        return False
    elif sorted(s1) == sorted(s2) and len(s1) - ham >= 1:
        return ham


print(max_ham("dear", "read"))
print(max_ham("dare", "read"))
print(max_ham("teardrop", "predated"))
print(max_ham("naive", "ravine"))
print(max_ham("solemn", "melons"))
print(max_ham("mister", "remits"))
print(max_ham("observe", "verbose"))
