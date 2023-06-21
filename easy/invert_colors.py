def color_invert(rgb):
    l = list(rgb)
    l[0] = abs(l[0]-255)
    l[1] = abs(l[1]-255)
    l[2] = abs(l[2]-255)
    return tuple(l)

print(color_invert((255, 255, 255)))
print(color_invert((0, 0, 0)))
print(color_invert((165, 170, 221)))