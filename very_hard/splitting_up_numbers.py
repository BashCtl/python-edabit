def num_split(num):
    temp = str(num) if num>0 else str(num)[1:]
    return [int(n) * (10 ** i) if num>0 else -int(n) * (10 ** i) for i, n in enumerate(str(temp)[::-1])][::-1]



# print(num_split(39))
print(num_split(-434))
