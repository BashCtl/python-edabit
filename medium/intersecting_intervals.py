def count_overlapping(intervals, point):
    return sum([1 if interval[0] <= point <= interval[1] else 0 for interval in intervals])


print(count_overlapping([[1, 2], [2, 3], [3, 4]], 5))
print(count_overlapping([[1, 2], [5, 6], [5, 7]], 5))
print(count_overlapping([[1, 2], [5, 8], [6, 9]], 7))