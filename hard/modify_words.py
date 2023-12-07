from unittest import TestCase

import math
"""
Modify Words

Create a function that takes a list of any length.
 Modify each element (capitalize, reverse, hyphenate).

Examples
edit_words(["new york city"]) ➞ ["YTIC KR-OY WEN"]

edit_words(["null", "undefined"]) ➞ ["LL-UN", "DENIF-EDNU"]

edit_words(["hello", "", "world"]) ➞ ["OLL-EH", "-", "DLR-OW"]

edit_words([""]) ➞ ["-"]

Notes
Input list values can be any type.

"""

def modify(word):
    word = word.upper()[::-1]
    l = len(word)
    mid = math.ceil(l / 2)
    return "-" if l == 0 else word[:mid] + "-" + word[mid:]


def edit_words(lst):
    return list(map(modify, lst))


TestCase().assertEqual(edit_words(["javascript"]), ["TPIRC-SAVAJ"])
TestCase().assertEqual(edit_words(["hello", "", "world"]), ["OLL-EH", "-", "DLR-OW"])
TestCase().assertEqual(edit_words(["null", "undefined"]), ["LL-UN", "DENIF-EDNU"])
TestCase().assertEqual(edit_words(["wood", "", "block"]), ["DO-OW", "-", "KCO-LB"])
TestCase().assertEqual(edit_words(["new york city"]), ["YTIC KR-OY WEN"])
TestCase().assertEqual(edit_words(["html", "css"]), ["LM-TH", "SS-C"])
TestCase().assertEqual(edit_words(["react", "vue", "angular"]), ["TCA-ER", "EU-V", "RALU-GNA"])
TestCase().assertEqual(edit_words(["11111", "999", "3333"]), ["111-11", "99-9", "33-33"])
TestCase().assertEqual(edit_words([""]), ["-"])
