def track_robot(instruction):
    position = [0, 0]
    for i in instruction:
        value = int(i.split()[1])
        direction = i.split()[0]
        if direction == "right":
            position[0] += value
        elif direction == "left":
            position[0] -= value
        elif direction == "up":
            position[1] += value
        else:
            position[1] -= value
    return position


print(track_robot(["right 10", "up 50", "left 30", "down 10"]))
print(track_robot([]))