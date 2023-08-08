def flip_list(lst):
    if len(lst) == 0:
        return lst
    elif type(lst[0]) == list:
        return [x for l in lst for x in l]
    else:
        return [[n] for n in lst]


# print(flip_list([1, 2, 3, 4]))
# print(flip_list([[5], [6], [9]]))

