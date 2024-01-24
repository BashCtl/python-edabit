"""
Find the Longest Word

Write a function that will return the longest word in a sentence.
In cases where more than one word is found, return the first one.

Examples
find_longest("A thing of beauty is a joy forever.") ➞ "forever"

find_longest("Forgetfulness is by all means powerless!") ➞ "forgetfulness"

find_longest("\"Strengths\" is the longest and most commonly used word that contains only a single vowel.") ➞ "strengths"

Notes
Special characters and symbols don't count as part of the word.
Return the longest word found in lowercase letters.
"""
import re


def find_longest(sentence):
    words = re.split("[^\\w]", sentence)
    return max(words, key=lambda a: len(a)).lower()


print(find_longest("A thing of beauty is a joy forever."))
