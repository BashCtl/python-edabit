"""
In the Centre?
Given a string containing mostly spaces and one non-space character, return whether the character is positioned in the very centre of the string. This means the number of spaces on both sides should be the same.

Examples
is_central("  #  ") ➞ True

is_central(" 2    ") ➞ False

is_central("@") ➞ True
Notes
Only one character other than spaces will be given at a time.
"""
import re
from unittest import TestCase


def is_central(txt):
    match = re.search(r"\S", txt)
    character_index = match.start()
    return len(txt[character_index + 1:]) == len(txt[:character_index])


TestCase().assertEqual(is_central('  #  '), True)
TestCase().assertEqual(is_central(' 2    '), False)
TestCase().assertEqual(is_central('@'), True)
TestCase().assertEqual(is_central(' 1'), False)
TestCase().assertEqual(is_central('7 '), False)
TestCase().assertEqual(is_central('  l '), False)
TestCase().assertEqual(is_central(' a  '), False)
TestCase().assertEqual(is_central('    G    '), True)
TestCase().assertEqual(is_central('   G     '), False)
TestCase().assertEqual(is_central('        %        '), True)
