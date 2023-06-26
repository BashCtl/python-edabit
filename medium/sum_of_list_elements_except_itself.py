def lst_ele_sum(args):
    return [sum(args) - element for element in args]


print(lst_ele_sum([1, 2, 3, 2, 1]))
print(lst_ele_sum([1, 2]))