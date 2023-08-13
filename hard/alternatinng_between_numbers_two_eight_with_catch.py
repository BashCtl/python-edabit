def f(n):
    try:
        n / int(str((n / 2)).split(".")[1])
    except ZeroDivisionError:
        return 8
    else:
        return 2


print(f(1))
print(f(2))
print(f(3))
print(f(6))
