def make_box(n):
    box = []
    for row in range(n):
        if row == 0 or row == n - 1:
            box.append("#" * n)
        else:
            box.append("#{}#".format(" " * (n - 2)))
    return box


print(make_box(5))
print(make_box(2))
print(make_box(1))
