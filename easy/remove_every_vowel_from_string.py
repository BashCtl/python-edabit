import re


def remove_vowels(txt):
    return re.sub(r'[aeiouAEIOU]', '', txt)


print(remove_vowels("I have never seen a thin person drinking Diet Coke."))