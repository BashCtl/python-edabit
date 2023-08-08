def find_fulcrum(lst):
    for index, value in enumerate(lst):
        if sum(lst[:index]) == sum(lst[index + 1:]):
            return value

    return -1


print(find_fulcrum([3, 1, 5, 2, 4, 6, -1]))
print(find_fulcrum([1, 2, 4, 9, 10, -10, -9, 3]))
print(find_fulcrum([9, 1, 9]))
print(find_fulcrum([7, -1, 0, -1, 1, 1, 2, 3]))
