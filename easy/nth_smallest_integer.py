def nth_smallest(lst, n):
    return sorted(lst)[n-1] if n-1 < len(lst) else None


print(nth_smallest([1, 3, 5, 7], 1))
print(nth_smallest([1, 3, 5, 7], 3))
print(nth_smallest([1, 3, 5, 7], 5))