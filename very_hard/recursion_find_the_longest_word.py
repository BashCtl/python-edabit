"""
Recursion: Find The Longest Word

Write a recursive function that will return the longest word in a sentence.
In cases where more than one word is found, return the first one.

Examples
find_longest("I will and ever will be gratefully and perpetually loving you Tesh!") ➞ "perpetually"

find_longest("A thing of beauty is a joy forever.") ➞ "forever"

find_longest("Forgetfulness is by all means powerless!") ➞ "forgetfulness"

find_longest("\"Strengths\" is the longest and most commonly used word that contains only a single vowel.") ➞ "strengths"

Notes
Special characters and symbols don't count as part of the word.
Return the longest word found in lowercase letters.
You are expected to solve this challenge via a recursive approach.

"""


import re


def find_longest(s, result=None):
    if not s:
        return result
    if type(s) == str:
        s = re.split(r"[^\w]", s.lower())
    if result is None or len(s[0]) > len(result):
        return find_longest(s[1:], s[0])

    return find_longest(s[1:], result)


from unittest import TestCase

str_vector = [
    "I will and ever will be gratefully and perpetually loving you Tesh!",
    "Hello darkness my old friend.", "Yourself is your soul's captain and fate's master.",
    "The pretty daughter's toy, a doll, is as pretty as her.",
    "A thing of beauty is a joy forever.", "Forgetfulness is by all means powerless!",
    "\"Strengths\" is the longest and most commonly used word that contains only a single vowel."
]
res_vector = [
    "perpetually", "darkness", "yourself", "daughter", "forever", "forgetfulness", "strengths"
]
for i, x in enumerate(str_vector):
    TestCase().assertEqual(find_longest(x), res_vector[i])
