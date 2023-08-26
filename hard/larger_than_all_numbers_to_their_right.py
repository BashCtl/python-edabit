def larger_than_right(lst):
    return [lst[i] for i in range(len(lst)) if i == len(lst)-1 or lst[i] > max(lst[i+1:])]
    # return list(filter(lambda item: item >= max(lst[lst.index(item):]), lst))


print(larger_than_right([3, 13, 11, 2, 1, 9, 5]))
print(larger_than_right([5, 9, 8, 7]))
print(larger_than_right([5, 5, 5, 5, 5, 5]))
