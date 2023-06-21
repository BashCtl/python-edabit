def index_multiplier(lst):
    return sum([lst[i] * i for i in range(0, len(lst))])


print(index_multiplier([1, 2, 3, 4, 5]))
print(index_multiplier([]))