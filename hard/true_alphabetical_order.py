"""
True Alphabetical Order

Create a function which takes every letter in every word,
and puts it in alphabetical order. Note how the original word lengths must stay the same.

Examples
true_alphabetic("hello world") ➞ "dehll loorw"

true_alphabetic("edabit is awesome") ➞ "aabdee ei imosstw"

true_alphabetic("have a nice day") ➞ "aaac d eehi nvy"

Notes
All sentences will be in lowercase.
No punctuation or numbers will be included in the Tests.
"""
import re


def true_alphabetic(txt: str):
    space_indexes = [space.start() for space in re.finditer(" ", txt)]
    letters = list(re.sub(" ", "", txt))
    letters = sorted(letters)
    for i in space_indexes:
        letters.insert(i, " ")
    return "".join(letters)


print(true_alphabetic("have a nice day"))
