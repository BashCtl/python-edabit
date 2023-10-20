def smallest_transform(num):
    nums = sorted(list(map(lambda n: int(n), list(str(num)))))
    median = nums[len(nums) // 2]
    return sum([abs(median - n) for n in nums])


print(smallest_transform(399))
print(smallest_transform(1234))
print(smallest_transform(153))
print(smallest_transform(33338))
