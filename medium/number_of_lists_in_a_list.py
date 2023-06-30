def num_of_sublists(lst):
    return sum([1 if type(item) == list else 0 for item in lst])


print(num_of_sublists([[1, 2, 3]]))
print(num_of_sublists([[1, 2, 3], [1, 2, 3], [1, 2, 3]]))
print(num_of_sublists([1, 2, 3]))