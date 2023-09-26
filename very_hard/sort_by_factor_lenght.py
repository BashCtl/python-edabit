def factor_sort(nums):
    func = lambda n: (factors(n), n)
    return sorted(nums, key=func, reverse=True)


def factors(nums):
    result = []
    i = 1
    while i * i <= nums:
        if nums % i == 0:
            result.append(i)
            if nums // i != i:
                result.append(nums // i)
        i += 1
    return len(result)


print(factory_sort([9, 7, 13, 12]))
