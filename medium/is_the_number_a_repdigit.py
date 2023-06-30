def is_repdigit(num):
    if num >= 0:
        return str(num).count(str(num)[0]) == len(str(num))
    return False


print(is_repdigit(66))
print(is_repdigit(0))
print(is_repdigit(-11))