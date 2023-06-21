def unique(lst):
    for number in lst:
        if lst.count(number) == 1:
            return number


print(unique([3, 3, 3, 7, 3, 3]))
print(unique([0, 0, 0.77, 0, 0]))
print(unique([0, 1, 1, 1, 1, 1, 1, 1]))