from collections import deque
from unittest import TestCase

"""
Burrows-Wheeler Transform

Burrows-Wheeler transform (BWT) is an algorithm which is used in data compression. 
Given a string text, BWT of text is a modified version of the string with same length as text. 
It can then be used to efficiently find substrings of text (which won't be covered here). 
We will just find the BWT of text.

Build Burrows-Wheeler-Matrix (BWM) containing all rotations of text.
Sort BWM lexicographically ($ < a < b < ... < z).
BWT is the last coloumn of BWM and gets returned.

# Example with text = "banana$"

# BWM (all rotations of text):
banana$
anana$b
nana$ba
ana$ban
na$bana
a$banan
$banana

# BWM sorted lexicographically:
$banana
a$banan
ana$ban
anana$b
banana$
na$bana
nana$ba

# BWT (last coloumn of BWM):
annb$aa

Examples
bw_transform("banana$") ➞ "annb$aa"

bw_transform("mississippi$") ➞ "ipssm$pissii"

bw_transform("acccgtttgtttcaatagatccatcaa$") ➞ "aacc$tacgttctaccatcaatatttgg"

Notes
Consider $ as the terminator character at the end of every input text.

"""


def bw_transform(text):
    arr = list(text)
    rotated = []
    d = deque(arr)
    for i in range(len(arr)):
        rotated.append("".join(list(d)))
        d.rotate(-1)
    result = ""
    for word in sorted(rotated):
        result += word[-1]
    return result


TestCase().assertEqual(bw_transform("banana$"), "annb$aa")
TestCase().assertEqual(bw_transform("mississippi$"), "ipssm$pissii")
TestCase().assertEqual(bw_transform("abaaba$"), "abba$aa")
TestCase().assertEqual(bw_transform("acccgtttgtttcaatagatccatcaa$"), "aacc$tacgttctaccatcaatatttgg")
