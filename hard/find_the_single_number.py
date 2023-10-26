def single_number(nums):
    for i in set(nums):
        if nums.count(i) == 1:
            return i


print(single_number([2, 2, 3, 2]))
print(single_number([0, 1, 0, 1, 0, 1, 99]))
print(single_number([-1, 2, -4, 20, -1, 2, -4, -4, 2, -1]))
