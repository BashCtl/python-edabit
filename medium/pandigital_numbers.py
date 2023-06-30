def is_pandigital(n):
    return len(set(str(n))) == 10


print(is_pandigital(98140723568910))
print(is_pandigital(90864523148909))
