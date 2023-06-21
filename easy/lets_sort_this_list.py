def asc_des_none(lst, s):
    if s == "Asc":
        return sorted(lst)
    if s == "Des":
        return list(reversed(sorted(lst)))
    return lst


print(asc_des_none([4, 3, 2, 1], "Asc"))
print(asc_des_none([7, 8, 11, 66], "Des"))
print(asc_des_none([1, 2, 3, 4], "None"))
