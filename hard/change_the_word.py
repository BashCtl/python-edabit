def change_string(word):
    word = word[::-1]

    def fun(l):
        if l.isupper() and l != "Z":
            return chr(ord(l) + 1)
        elif l == "Z":
            return "A"
        return l

    return "".join(list(map(fun, word))).upper()



print(change_string("ApPle"))
print(change_string("draGON"))
print(change_string("ZebrA"))
