"""
Alphabetically Sorted

A word is alphabetically sorted if all of the letters in it are in consecutive alphabetical order.
Some examples of alphabetically sorted words: abhors (a is before b, b is before h, h is before o, etc.),
ghost, accent, hoop.

Create a function that takes in a sentence as input and returns
True if there is at least one alphabetically sorted word inside that has a minimum length of 3.

Examples
is_alphabetically_sorted("Paula has a French accent.") ➞ True
# "accent" is alphabetically sorted.

is_alphabetically_sorted("The biopsy returned negative results.") ➞ True
# "biopsy" is alphabetically sorted.

is_alphabetically_sorted("She sells sea shells by the sea shore.") ➞ False
# Although "by" is alphabetically sorted, it is only 2 letters long.

Notes
Do not count words with 2 or fewer characters.
Ignore punctuation (periods, commas, etc).
"""
import string


def is_alphabetically_sorted(sentence):
    sentence = sentence.translate(str.maketrans("", "", string.punctuation)).split(" ")
    return any([len(word) > 2 and list(word) == sorted(list(word)) for word in sentence])


print(is_alphabetically_sorted("Paula has a French accent."))
print(is_alphabetically_sorted("She sells sea shells by the sea shore."))