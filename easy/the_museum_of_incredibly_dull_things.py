def remove_smallest(lst):
    if len(lst)>1:
        m = min(lst)
        lst.remove(m)
        return lst
    return []


print(remove_smallest([5, 3, 2, 1, 4]))
print(remove_smallest([2, 2, 1, 2, 1]))
