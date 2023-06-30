def valid_division(d):
    d = d.replace("/", "%")
    try:
        return eval(d) == 0
    except ZeroDivisionError:
        return "invalid"


print(valid_division("6/3"))
print(valid_division("30/25"))
print(valid_division("0/3"))
print(valid_division("0/0"))
