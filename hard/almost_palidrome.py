def almost_palindrome(txt):
    reversed_txt = txt[::-1]
    return len([i for i in range(len(txt)) if txt[i] != reversed_txt[i]]) == 2


print(almost_palindrome("abcdcbg"))
print(almost_palindrome("abcdaaa"))
