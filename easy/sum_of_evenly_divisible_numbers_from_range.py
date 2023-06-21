def evenly_divisible(a, b, c):
    even = [x for x in range(a, b + 1) if x % c == 0]
    return sum(even)


print(evenly_divisible(1, 10, 20))
print(evenly_divisible(1, 10, 2))
