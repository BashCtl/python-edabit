def bitwise_index(lst):
    index = None
    max_even = -1
    for i, v in enumerate(lst):
        if v & 1 == 0 and v >= max_even:
            max_even = v
            index = i
    if index is None:
        return "No even integer found!"
    elif index & 1 == 0:
        return {"@even index {}".format(index): max_even}
    elif index & 1 == 1:
        return {"@odd index {}".format(index): max_even}


#
# print(bitwise_index([107, 19, 36, -18, -78, 24, 97]))
# print(bitwise_index([31, 7, 2, 13, 7, 9, 10, 13]))
# print(bitwise_index([4, 4, 4, 4, 4, 4]))
# print(bitwise_index([-31, -7, -13, -7, -9, -13]))
print(bitwise_index([-84, -42, 0, -2, -94, -8]))
