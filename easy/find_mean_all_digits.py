def mean(num):
    return int(sum([int(x) for x in str(num)]) / len(str(num)))


print(mean(42))
print(mean(666))