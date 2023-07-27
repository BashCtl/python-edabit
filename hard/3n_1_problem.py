def collatz(a, b):
    while True:
        if a % 2 == 0:
            a //= 2
        if a == 1:
            return "a"
        if a % 2 != 0:
            a = a * 3 + 1
        if b % 2 == 0:
            b //= 2
        if b == 1:
            return "b"
        if b % 2 != 0:
            b = b * 3 + 1


print(collatz(10, 15))
print(collatz(13, 16))
print(collatz(53782, 72534))
