def find_the_difference(s, t):
    for i in s:
        if i in t:
            t = t.replace(i, "", 1)
    return t


print(find_the_difference("abcd", "abcde"))
print(find_the_difference("ae", "aea"))
