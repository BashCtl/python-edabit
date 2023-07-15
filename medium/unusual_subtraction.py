def not_good_math(n, k):
    while k:
        if str(n)[-1] == "0":
            n //= 10
        else:
            n -= 1
        k -= 1
    return n


print(not_good_math(540, 5))
print(not_good_math(1000000000, 9))
