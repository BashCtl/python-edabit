import re


def replace_vowels(txt, ch):
    return re.sub("[aeiou]", ch, txt)


print(replace_vowels("the aardvark", "#"))