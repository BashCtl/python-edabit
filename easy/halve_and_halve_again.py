def halve_count(a, b):
    count = -1
    while a > b:
        a /= 2
        count += 1
    return count


print(halve_count(1324, 98))
print(halve_count(624, 8))
