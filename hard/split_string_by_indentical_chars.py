"""
Split String by Identical Characters

Create a function that splits a string into an array of identical clusters.

Examples
split_groups("555") ➞ ["555"]

split_groups("5556667788") ➞ ["555", "666", "77", "88"]

split_groups("aaabbbaabbab") ➞ ["aaa", "bbb", "aa", "bb", "a", "b"]

split_groups("abbbcc88999&&!!!_") ➞ ["a", "bbb", "cc", "88", "999", "&&", "!!!", "_"]
Notes
Each cluster should only have one unique character.
The resulting array should be in the same order as the input string.
Should work with letters, numbers and other characters.

"""

from itertools import groupby


def split_groups(txt):
    return ["".join(c) for _, c in groupby(txt)]


print(split_groups("aaabbbaabbab"))