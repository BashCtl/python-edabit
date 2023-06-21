def clone(lst):
    lst.append(lst[:])
    return lst


print(clone([1,1]))