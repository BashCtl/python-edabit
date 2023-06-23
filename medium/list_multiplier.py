def multiply(l):
    return [[item for i in range(len(l))] for item in l]


print(multiply([4, 5]))
print(multiply(["*", "%", "$"]))
