def is_symmetrical(num):
    return num == int(str(num)[::-1])


print(is_symmetrical(7227))
print(is_symmetrical(12567))
