def count_ones(num):
    return bin(num).count('1')


print(count_ones(0))
print(count_ones(100))
print(count_ones(999))
