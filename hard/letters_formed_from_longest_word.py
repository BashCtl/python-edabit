"""
Letters Formed from the Longest Word

Write a function that returns True if all the lst in a list can be formed by using
only the characters from the longest string.

Examples
can_form(["mast", "manifest", "met", "fan"]) ➞ True

can_form(["may", "master", "same", "reams"]) ➞ False

can_form(["may", "same", "reams", "mastery"]) ➞ True
Notes
There will only be one unique longest string.


"""

from itertools import permutations


def can_form(lst):
    longest_word = max(lst, key=len)
    return all(longest_word.count(i) >= word.count(i) for word in lst for i in set(word))


print(can_form(["mast", "manifest", "met", "fan"]))
