import re


def count_lone_ones(n):
    pattern = r"(?<![1])[1](?![1])"
    return len(re.findall(pattern, str(n)))


print(count_lone_ones(101))
print(count_lone_ones(1191))
print(count_lone_ones(1111))
print(count_lone_ones(462))