def min_length(lst, n):
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)+1):
            if sum(lst[i:j]) > n:
                result.append(len(lst[i:j]))
    return min(result) if len(result) > 0 else -1


print(min_length([5, 8, 2, -1, 3, 4], 9))
print(min_length([3, -1, 4, -2, -7, 2], 4))
print(min_length([1, 0, 0, 0, 1], 1))
print(min_length([0, 1, 1, 0], 2))
