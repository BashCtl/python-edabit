def steps_to_convert(txt):
    lower = len([i for i in txt if i.islower()])
    upper = len([i for i in txt if i.isupper()])
    return min(lower, upper)


print(steps_to_convert("abC"))
print(steps_to_convert("abCBA"))
print(steps_to_convert("aba"))
print(steps_to_convert("abaCCC"))