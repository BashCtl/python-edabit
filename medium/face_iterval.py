def face_interval(num):
    if type(num) != list:
        return ":/"
    num.sort()
    interval = num[-1] - num[0]
    return ":)" if interval in num else ":("


print(face_interval([1, 2, 5, 8, 3, 9]))
print(face_interval([5, 2, 8, 3, 11]))
print(face_interval("bruh"))