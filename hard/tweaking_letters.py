def tweak_letters(txt, lst):
    result = []
    for l, i in zip(txt, lst):
        if l == "a" and i == -1:
            result.append("z")
        elif l == "z" and i == 1:
            result.append("a")
        else:
            result.append(chr(ord(l)+i))
    return "".join(result)

print(tweak_letters("apple", [0, 1, -1, 0, -1]))
print(tweak_letters("many", [0, 0, 0, -1]))
