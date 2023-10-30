"""
Nearest Vowel

Given a letter, created a function which returns the nearest
vowel to the letter. If two vowels are equidistant
to the given letter, return the earlier vowel.

Examples
nearest_vowel("b") ➞ "a"

nearest_vowel("s") ➞ "u"

nearest_vowel("c") ➞ "a"

nearest_vowel("i") ➞ "i"

Notes
All letters will be given in lowercase.
There will be no alphabet wrapping involved,
meaning the closest vowel to "z" should return "u", not "a".
"""
import string


def nearest_vowel(s):
    alphabet = string.ascii_lowercase
    vowels = "aeiou"
    diff = 29
    result = ""
    for v in vowels:
        if abs(alphabet.index(v) - alphabet.index(s)) < diff:
            diff = abs(alphabet.index(v) - alphabet.index(s))
            result = v
    return result


print(nearest_vowel("b"))
print(nearest_vowel("s"))
print(nearest_vowel("c"))
print(nearest_vowel("i"))
print(nearest_vowel("z"))
print(nearest_vowel("g"))
