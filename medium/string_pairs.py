"""
String Pairs
Create a function that takes a string s and returns a list of two-paired characters. If the string has an odd number of characters, add an asterisk * in the final pair.

See the below examples for a better understanding:

Examples
string_pairs("mubashir") ➞ ["mu", "ba", "sh", "ir"]

string_pairs("edabit") ➞ ["ed", "ab", "it"]

string_pairs("airforces") ➞ ["ai", "rf", "or", "ce", "s*"]
Notes
Return [] if the given string is empty.


"""

import re
from unittest import TestCase


def string_pairs(s):
    result = re.findall("." * 2, s)
    return result if len(s) % 2 == 0 else result + [s[-1] + "*"]


TestCase().assertEqual(string_pairs("abcdef"), ["ab", "cd", "ef"])
TestCase().assertEqual(string_pairs("abcdefg"), ["ab", "cd", "ef", "g*"])
TestCase().assertEqual(string_pairs(""), [])
TestCase().assertEqual(string_pairs("pak"), ["pa", "k*"])
TestCase().assertEqual(string_pairs("mubashir"), ["mu", "ba", "sh", "ir"])
TestCase().assertEqual(string_pairs("edabit"), ["ed", "ab", "it"])
TestCase().assertEqual(string_pairs("airforces"), ["ai", "rf", "or", "ce", "s*"])
