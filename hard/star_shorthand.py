"""
Star Shorthand

Write a function that converts a string into star shorthand. If a character is repeated n times, convert it into character*n.

Examples
to_star_shorthand("abbccc") ➞ "ab*2c*3"

to_star_shorthand("77777geff") ➞ "7*5gef*2"

to_star_shorthand("abc") ➞ "abc"

to_star_shorthand("") ➞ ""
Notes
Leave lone occurrences of a character as is.
Return an empty string if given an empty string input.


"""

from unittest import TestCase

import re


def to_star_shorthand(s):
    if not s:
        return ""
    pattern = re.compile(r'(.)\1*')

    def replacer(match):
        char = match.group(0)
        if len(char) > 1:
            return f"{char[0]}*{len(char)}"
        else:
            return char

    # Apply the replacer function to each match
    return pattern.sub(replacer, s)


TestCase().assertEqual(to_star_shorthand("abbccc"), "ab*2c*3")
TestCase().assertEqual(to_star_shorthand("haaaappyyyyy"), "ha*4p*2y*5")
TestCase().assertEqual(to_star_shorthand("77777geff"), "7*5gef*2")
TestCase().assertEqual(to_star_shorthand("11223344"), "1*22*23*24*2")
TestCase().assertEqual(to_star_shorthand("abc"), "abc")
TestCase().assertEqual(to_star_shorthand(""), "")
