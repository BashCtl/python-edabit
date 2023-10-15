def block(lst):
    result = 0
    for i in range(len(lst)):
        if 2 in lst[i]:
            result += (len(lst) - i - 1) * lst[i].count(2)
    return result


print(block([
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 2],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]))

print(block([
    [1, 2, 1, 1],
    [1, 1, 1, 2],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]))

print(block([
    [1, 1, 1, 1],
    [2, 1, 1, 2],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]))

print(block([
  [1, 2, 1, 1],
  [2, 1, 1, 2]
]))
