
def dice_game(lst):
    total = sum([i + j for i, j in lst])
    for x, y in lst:
        if x == y:
            return 0
    return total


print(dice_game([(1, 2), (3, 4), (5, 6)]))
print(dice_game([(1, 1), (5, 6), (6, 4)]))
