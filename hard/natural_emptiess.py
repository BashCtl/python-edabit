def rep_set(n):
    if n == 0:
        return []
    return rep_set(n - 1) + [rep_set(n - 1)]


print(rep_set(2))
