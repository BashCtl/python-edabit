def happy(n):
    while True:
        if n == 1:
            return True
        elif n == 4:
            return False
        n = sum([int(number) ** 2 for number in list(str(n))])


print(happy(203))
print(happy(11))
print(happy(107))