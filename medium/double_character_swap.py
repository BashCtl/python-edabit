import re


def double_swap(txt, c1, c2):
    return re.sub(f"[{c2}{c1}]", lambda f: {c1: c2, c2: c1}[f.group()], txt)


print(double_swap("aabbccc", "a", "b"))
