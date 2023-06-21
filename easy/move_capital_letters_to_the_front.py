import re


def cap_to_front(s):
    upper = "".join([l for l in s if l.isupper()])
    lower = "".join([l for l in s if l.islower()])
    return upper + lower


print(cap_to_front("hApPy"))
print(cap_to_front("moveMENT"))
