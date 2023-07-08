import re


def cap_space(txt):
    return " ".join(re.findall("[a-zA-Z][^A-Z]*", txt)).lower()


print(cap_space("iLoveMyTeapot"))
print(cap_space("stayIndoors"))
