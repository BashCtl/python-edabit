def rolling_cipher(txt, n):
    result = []
    for l in txt:
        if ord(l)+n > ord("z"):
            result.append(chr(ord("a") + ord(l)+n-ord("z")-1))
        elif ord(l)+n<ord("a"):
            result.append(chr(ord("z") + ord("a")-ord(l)+n+1))
        else:
            result.append(chr(ord(l)+n))

    return "".join(result)


print(rolling_cipher("abcd", 1))
print(rolling_cipher("abcd", -1))
print(rolling_cipher("abcd", 3))
print(rolling_cipher("abcd", 26))