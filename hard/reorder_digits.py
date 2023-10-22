def reorder_digits(lst, direction):
    fun = lambda i: int(i) if direction == "asc" else -int(i)
    return [int("".join(sorted(list(str(num)), key=fun))) for num in lst]


print(reorder_digits([515, 341, 98, 44, 211], "asc"))

print(reorder_digits([515, 341, 98, 44, 211], "desc"))
