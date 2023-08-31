def split(txt):
    result = []
    temp = list(txt)
    s = ""
    while len(temp) > 0:
        s += temp.pop(0)
        if s[0] != s[-1] and s.count(s[0]) == s.count(s[-1]):
            result.append(s)
            s = ""
    return result


print(split("()()()"))
print(split("((()))"))
print(split("((()))(())()()(()())"))
print(split("((())())(()(()()))"))
