import re


def count_ones(lst):
    text = "".join(map(str,lst))
    return len(re.findall(r"1{2,}", text))


print(count_ones([1, 0, 0, 1, 1, 0, 1, 1, 1]))
print(count_ones([1, 0, 1, 0, 1, 0, 1, 0]))
print(count_ones([1, 1, 1, 1, 0, 0, 0, 0]))