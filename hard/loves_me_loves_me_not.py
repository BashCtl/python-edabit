def loves_me(n):
    loves = ["Loves me" if i%2!=0 else "Loves me not" for i in range(1, n+1)]
    loves[-1] = loves[-1].upper()
    return ", ".join(loves)


print(loves_me(3))
print(loves_me(6))
print(loves_me(1))