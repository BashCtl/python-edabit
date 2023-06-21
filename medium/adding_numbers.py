def add(n1, n2):
    try:
        return "{}".format(int(n1) + int(n2))
    except:
        return "Invalid Operation"


print(add("111", "111"))
print(add("", "111"))