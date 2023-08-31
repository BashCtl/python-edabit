import re


def is_match(s, p):
    return re.match("^{}$".format(p), s) is not None


print(is_match("aa", "a"))
print(is_match("aa", "a*"))
print(is_match("ab", ".*"))
