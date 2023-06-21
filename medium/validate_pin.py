import re


def valid(txt):
    return re.search(r"^(\d{4}|\d{6})$", txt) is not None


print(valid("1234"))
print(valid(" 45135"))
print(valid("45dd57"))
print(valid("456897"))
