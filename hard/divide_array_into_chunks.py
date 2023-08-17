def chunkify(lst, size):
    return [lst[i:i + size] for i in range(0, len(lst), size)]


print(chunkify([2, 3, 4, 5], 2))
print(chunkify([2, 3, 4, 5, 6], 2))
print(chunkify([2, 3, 4, 5, 6, 7], 3))
print(chunkify([2, 3, 4, 5, 6, 7], 1))
print(chunkify([2, 3, 4, 5, 6, 7], 7))
