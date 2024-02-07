"""
Meme Sum :)

Examples
meme_sum(26, 39) ➞ 515
# 2+3 = 5, 6+9 = 15
# 26 + 39 = 515

meme_sum(122, 81) ➞ 1103
# 1+0 = 1, 2+8 = 10, 2+1 = 3
# 122 + 81 = 1103

meme_sum(1222, 30277) ➞ 31499

"""


def meme_sum(a, b):
    a = str(a)
    b = str(b)
    max_length = max(len(a), len(b))
    a = a.zfill(max_length)
    b = b.zfill(max_length)
    s_num = "".join([str(int(x) + int(y)) for x, y in zip(list(a), list(b))])
    return int(s_num)


print(meme_sum(26, 39))
print(meme_sum(122, 81))
