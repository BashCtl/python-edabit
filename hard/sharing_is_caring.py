from functools import reduce


def show_the_love(lst):
    min_value = min(lst)
    min_index = lst.index(min_value)
    for index, value in enumerate(lst):
        if index != min_index:
            lst[min_index] += value * 0.25
            lst[index] = value * 0.75
    return lst


print(show_the_love([4, 1, 4]))
