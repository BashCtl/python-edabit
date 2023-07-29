def rearranged_difference(num):
    nums = sorted(str(num))
    return int("".join(nums[::-1])) -int("".join(nums))


print(rearranged_difference(972882))
