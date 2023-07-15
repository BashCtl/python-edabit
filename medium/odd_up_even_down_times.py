def even_odd_transform(lst, n):
    return [item - 2 * n if item % 2 == 0 else item + 2 * n for item in lst]


print(even_odd_transform([3, 4, 9], 3))
print(even_odd_transform([0, 0, 0], 10))
