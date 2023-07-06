import re


def to_scottish_screaming(txt):
    return re.sub("[aeiou]", "e", txt.lower()).upper()


print(to_scottish_screaming("hello world"))