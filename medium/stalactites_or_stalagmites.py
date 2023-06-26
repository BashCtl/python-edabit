def mineral_formation(cave):
    is_stalactites = 1 in cave[0]
    is_stalagmites = 1 in cave[-1]
    return "stalactites" if is_stalactites and not is_stalagmites else "stalagmites" if is_stalagmites and not is_stalactites else "both"


cave1 = [
    [0, 1, 0, 1],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]
cave2 = [
    [0, 0, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 1, 1, 1]
]

cave3 = [
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 1, 1, 1]
]

print(mineral_formation(cave1))
print(mineral_formation(cave2))
print(mineral_formation(cave3))
