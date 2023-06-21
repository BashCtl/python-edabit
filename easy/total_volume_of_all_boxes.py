from functools import reduce


def total_volume(*boxes):
    squares = []
    for items in boxes:
        squares.append(reduce(lambda a, b: a * b, items))
    return sum(squares)


print(total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]))
