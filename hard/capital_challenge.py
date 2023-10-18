def select_letters(s1, s2):
    first = []
    second = []
    for x, y in zip(s1, s2):
        if y.isupper():
            first.append(x)
        if x.isupper():
            second.append(y)
    return "".join(first+second)


print(select_letters("heLLO", "GUlp"))
print(select_letters("1234567", "XxXxX"))
print(select_letters("EVERYTHING", "SomeThings"))
print(select_letters("PaTtErN", "pAtTeRn"))
