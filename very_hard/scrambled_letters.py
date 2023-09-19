import re


def scrambled(words, mask):
    mask = "^" + mask.replace("*", ".") + "$"
    return [word for word in words if re.search(mask, word)]


print(scrambled(["red", "dee", "cede", "reed", "creed", "decree"], "*re**"))
print(scrambled(["red", "dee", "cede", "reed", "creed", "decree"], "***"))
