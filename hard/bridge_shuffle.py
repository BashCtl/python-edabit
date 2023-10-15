def bridge_shuffle(lst1, lst2):
    result = []
    for x, y in zip(lst1, lst2):
        result.append(x)
        result.append(y)

    if len(lst1) > len(lst2):
        result += lst1[len(lst2):]
    elif len(lst1) < len(lst2):
        result += lst2[len(lst1):]

    return result


print(bridge_shuffle(["A", "A", "A"], ["B", "B", "B"]))
print(bridge_shuffle(["C", "C", "C", "C"], ["D"]))
print(bridge_shuffle([1, 3, 5, 7], [2, 4, 6]))
