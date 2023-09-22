"""
Esthetic Numbers

A number is Esthetic if, in any base from base2 up to base10, the absolute difference
between every pair of its adjacent digits is constantly equal to 1.

num = 441 (base10)
# Adjacent pairs of digits:
# |4, 4|, |4, 1|
# The absolute difference is not constant
# 441 is not Esthetic in base10

441 in base4 = 12321
# Adjacent pairs of digits:
# |1, 2|, |2, 3|, |3, 2|, |2, 1|
# The absolute difference is constant and is equal to 1
# 441 is Esthetic in base4

esthetic(10) ➞ [2, 3, 8, 10]
# 10 in base2 = 1010
# 10 in base3 = 101
# 10 in base8 = 12
# 10 in base10 = 10

esthetic(23) ➞ [3, 5, 7, 10]
# 23 in base3 = 212
# 23 in base5 = 43
# 23 in base7 = 32
# 23 in base10 = 23

esthetic(666) ➞ [8]
# 666 in base8 = 1232
"""


def convert_to_base(num, base):
    a = 0
    i = 0
    r = 0
    while num:
        num, r = divmod(num, base)
        a += 10 ** i * r
        i += 1

    return a


def esthetic(num):
    nums = {b: convert_to_base(num, b) for b in range(2, 11)}
    result = []
    for k, v in nums.items():
        s_num = str(v)
        esth = all([abs(int(s_num[i]) - int(s_num[i + 1])) == 1 for i in range(len(s_num) - 1)])
        if esth:
            result.append(k)
    return result if result else "Anti-Esthetic"


print(esthetic(10))
print(esthetic(23))
print(esthetic(666))
print(esthetic(74))
