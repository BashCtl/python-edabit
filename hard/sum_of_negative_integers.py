import re


def negative_sum(chars):
    return eval(re.sub(r"\b(?<!-)[\d%& \w]+", "", chars))


print(negative_sum("-12 13%14&-11"))
print(negative_sum("22 13%14&-11-22 13 12"))
print(negative_sum("33%14&-1 12 a 21 -2 b c"))
