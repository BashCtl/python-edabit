def count_missing_nums(lst):
    lst = [int(n) for n in lst if n.isdigit()]
    lst.sort()
    return sum([lst[i + 1] - lst[i] - 1 for i in range(len(lst) - 1)])



print(count_missing_nums(["1", "3", "5", "7", "9"]))
print(count_missing_nums(["1", "5", "B", "9", "z"]))
print(count_missing_nums(["7", "3", "1", "9", "5"]))
print(count_missing_nums(['1', '78', 'B', '9', 'z']))
