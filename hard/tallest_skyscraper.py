def tallest_skyscraper(lst):
    length = len(lst)
    for i in range(length):
        if 1 in lst[i]:
            return length - i


data1 = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 1]
]

print(tallest_skyscraper(data1))

data2 = [
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [1, 1, 1, 1]
]

print(tallest_skyscraper(data2))
