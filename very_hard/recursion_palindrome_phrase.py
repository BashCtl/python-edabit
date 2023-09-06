def is_palindrome(p: str):
    p = "".join([s for s in p.lower() if s.isalpha()])
    if len(p) == 0:
        return True
    return p[0] == p[-1] and is_palindrome(p[1:-1])


print(is_palindrome("Go hang a salami, I'm a lasagna hog!"))
print(is_palindrome("This phrase, surely, is not a palindrome!"))
