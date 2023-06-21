def first_and_last(s):
    s = ''.join(sorted(s))
    return [s, s[::-1]]


print(first_and_last("marmite"))
print(first_and_last("bench"))
print(first_and_last("scoop"))