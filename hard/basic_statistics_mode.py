def mode(nums):
    m = max([nums.count(n) for n in set(nums)])
    return sorted(list(filter(lambda a: nums.count(a) == m, set(nums))))


print(mode([4, 5, 6, 6, 6, 7, 7, 9, 10]))
print(mode([4, 5, 5, 6, 7, 8, 8, 9, 9]))
print(mode([1, 2, 2, 3, 6, 6, 7, 9]))
