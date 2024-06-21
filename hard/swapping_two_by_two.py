"""
Swapping Two by Two

Write a function that swaps the first pair (1st and 2nd characters) with the second pair (3rd and 4th characters) for every quadruplet substring.

Examples
swap_two("ABCDEFGH") ➞ "CDABGHEF"

swap_two("AABBCCDDEEFF") ➞ "BBAADDCCFFEE"

swap_two("munchkins") ➞ "ncmuinhks"

swap_two("FFGGHHI") ➞ "GGFFHHI"
Notes
Keep leftover strings in the same order.
"""

import re

from unittest import TestCase


def swap_two(txt):
    pattern = re.compile(r"([\w]{2})([\w]{2})")
    return pattern.sub("\g<2>\g<1>", txt)


TestCase().assertEqual(swap_two("ABCDEFGH"), "CDABGHEF")
TestCase().assertEqual(swap_two("AABBCCDDEEFF"), "BBAADDCCFFEE")
TestCase().assertEqual(swap_two("oompaloompa"), "mpooooalmpa")
TestCase().assertEqual(swap_two("munchkins"), "ncmuinhks")
TestCase().assertEqual(swap_two("FFGGHHI"), "GGFFHHI")
TestCase().assertEqual(swap_two("FFG"), "FFG")
TestCase().assertEqual(swap_two(""), "")
