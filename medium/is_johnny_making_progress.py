def progress_days(runs):
    return sum([1 if runs[i + 1] - runs[i] >= 1 else 0 for i in range(len(runs) - 1)])


print(progress_days([3, 4, 1, 2]))
print(progress_days([10, 11, 12, 9, 10]))
print(progress_days([6, 5, 4, 3, 2, 9]))
print(progress_days([9,9]))