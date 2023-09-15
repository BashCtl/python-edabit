import math


def climb(stamina, obstacles):
    result = 0
    for i in range(len(obstacles) - 1):
        current = obstacles[i]
        next = obstacles[i + 1]
        diff = next - current
        if diff < 0:
            stamina -= math.ceil(abs(diff))
        else:
            stamina -= math.ceil(diff) * 2
        if stamina >= 0:
            result += 1
        else:
            break
    return result


print(climb(5, [5, 4.2, 3, 3.5, 6, 4, 6, 8, 1]))
print(climb(10, [5, 4.2, 3, 3.5, 6, 4, 6, 8, 1]))
