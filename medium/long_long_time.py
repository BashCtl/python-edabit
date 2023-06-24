def longest_time(h, m, s):
    if h > max(m / 60, s / (60 * 60)):
        return h
    elif m / 60 > max(h, s / (60 * 60)):
        return m
    return s


print(longest_time(1, 59, 3598))
print(longest_time(2, 300, 15000))
print(longest_time(15, 955, 59400))
