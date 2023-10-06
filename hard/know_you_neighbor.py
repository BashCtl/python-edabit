import re


def plus_sign(txt):
    pattern = r"(?<=\+)[a-z](?=\+)"
    letters = re.sub("[^a-z]", "", txt)
    return len(re.findall(pattern, txt)) == len(letters)


print(plus_sign("+f+d+c+#+f+"))
print(plus_sign("+d+=3=+s+"))
print(plus_sign("f++d+g+8+"))
print(plus_sign("+s+7+fg+r+8+"))
