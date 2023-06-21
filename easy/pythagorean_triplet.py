def is_triplet(n1, n2, n3):
    num = [n1, n2, n3]
    num = sorted(num)
    return num[0] * num[0] + num[1] * num[1] == num[2] * num[2]


print(is_triplet(3, 4, 5))
print(is_triplet(1, 2, 4))
print(is_triplet(13, 5, 12))
