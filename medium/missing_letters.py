import re
import string


def get_missing_letters(s):
    all_letters = string.ascii_lowercase
    return re.sub("[" + s + "]", "", all_letters) if len(s)!=0 else all_letters


print(get_missing_letters("abcdefgpqrstuvwxyz"))
print(get_missing_letters("abc"))
