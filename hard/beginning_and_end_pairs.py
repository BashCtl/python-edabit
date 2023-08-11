def pairs(lst):
    mid = len(lst) // 2
    if len(lst) % 2 == 0:
        return [[lst[i], lst[len(lst) - i - 1]] for i in range(mid)]
    else:
        return [[lst[i], lst[len(lst) - i - 1]] for i in range(mid)] + [[lst[mid], lst[mid]]]


print(pairs([1, 2, 3, 4, 5, 6]))
print(pairs([1, 2, 3, 4, 5, 6, 7]))
print(pairs([5, 9, 8, 1, 2]))
