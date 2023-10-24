def fib_str(n, txt):
    for i in range(2, n):
        txt.append(txt[i-1]+txt[i-2])
    return ", ".join(txt)


print(fib_str(3, ["j", "h"]))
print(fib_str(5, ["e", "a"]))