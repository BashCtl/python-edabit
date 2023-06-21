import re


def left_digit(num):
    return int(re.sub(r"\D", '', num)[0])


print(left_digit("TrAdE2W1n95!"))
print(left_digit("U//DertHe1nflu3nC3"))
