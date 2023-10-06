import re


def count_same_ends(txt):
    words = re.sub("[^\w ]", "", txt.lower()).split(" ")
    return len([w for w in words if w[0] == w[-1] and len(w) > 1])


print(count_same_ends("Pop! goes the balloon"))
print(count_same_ends("And the crowd goes wild!"))
print(count_same_ends("No I am not in a gang."))
