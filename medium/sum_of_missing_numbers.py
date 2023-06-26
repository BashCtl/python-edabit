def sum_missing_numbers(lst):
    max_sum = sum([item for item in range(min(lst), max(lst)+1)])
    return max_sum - sum(lst)


print(sum_missing_numbers([4, 3, 8, 1, 2]))
print(sum_missing_numbers([17, 16, 15, 10, 11, 12]))
