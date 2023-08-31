def can_see_stage(seats):
    for i in range(len(seats)):
        for j in range(len(seats) - 1, 0, -1):
            if seats[j][i] - seats[j - 1][i] <= 0:
                return False
    return True


print(can_see_stage([
    [0, 0, 0],
    [1, 1, 1],
    [2, 2, 2]
]))

print(can_see_stage(
    [
        [2, 0, 0],
        [1, 1, 1],
        [2, 2, 2]
    ]
))

print(can_see_stage([
  [1, 0, 0],
  [1, 1, 1],
  [2, 2, 2]
]))