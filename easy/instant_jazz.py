def jazzify(lst):
    if len(lst) == 0:
        return lst
    else:
        for x in range(len(lst)):
            if lst[x][-1] != "7":
                lst[x] += "7"
    return lst


print(jazzify(["G", "F", "C"]))
print(jazzify(["G", "F7", "C"]))
print(jazzify([]))
