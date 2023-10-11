def possible_palindrome(txt):
    count = 0
    for l in set(txt):
        if txt.count(l) % 2 != 0:
            count += 1
        if count > 1:
            return False
    return True


print(possible_palindrome("acabbaa"))
print(possible_palindrome("aacbdbc"))
print(possible_palindrome("aacbdb"))
print(possible_palindrome("abacbb"))