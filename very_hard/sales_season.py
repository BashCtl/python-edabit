def discount(lst):
    total = sum(lst)
    if len(lst) >= 12:
        free = sum(sorted(lst)[:4])
    elif len(lst) >= 9:
        free = sum(sorted(lst)[:3])
    elif len(lst) >= 6:
        free = sum(sorted(lst)[:2])
    elif len(lst) > 2:
        free = min(lst)
    else:
        return lst
    dis = (total - free) / total
    return [round(price * dis, 2) for price in lst]


print(discount([2.99, 5.75, 3.35, 4.99]))
print(discount([5.75, 14.99, 36.83, 12.15, 25.30, 5.75, 5.75, 5.75]))
