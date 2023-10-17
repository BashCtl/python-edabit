import math


def lengthen(s1, s2):
    min_s = min(s1, s2, key=len)
    max_s = max(s1, s2, key=len)
    result = min_s * math.ceil(len(max_s) / len(min_s))
    return result[:len(max_s)]


print(lengthen("abcdefg", "ab"))
print(lengthen("ingenius", "forest"))
print(lengthen("clap", "skipping"))
