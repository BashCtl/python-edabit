def find_odd(lst):
    unique = set(lst)
    for n in unique:
        if lst.count(n) % 2 != 0:
            return n


print(find_odd([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]))
