def fibo_word(n):
    if n < 2:
        return "invalid"
    fib_lst = ["b", "a"]
    for i in range(2, n):
        fib_lst.append(fib_lst[i - 1] + fib_lst[i - 2])
    return ", ".join(fib_lst)


print(fibo_word(1))
print(fibo_word(3))
print(fibo_word(7))
