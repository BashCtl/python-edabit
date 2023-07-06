import re


def censor(s):
    return re.sub("[\\w]{5,}", lambda a: "*" * len(a.group()), s)


print(censor("The code is fourty"))
