"""
Valid Rondo Form?
Rondo Form is a type of musical structure, in which there is a recurring theme/refrain, notated as A. Here are the rules for valid rondo forms:

Rondo forms always start and end with an A section.
In between the A sections, there should be contrasting sections notated as B, then C, then D, etc... No letter should be skipped.
There shouldn't be any repeats in the sequence (such as ABBACCA).
Create a function which validates whether a given string is a valid Rondo Form.

Examples
valid_rondo("ABACADAEAFAGAHAIAJA") ➞ True

valid_rondo("ABA") ➞ True

valid_rondo("ABBACCA") ➞ False

valid_rondo("ACAC") ➞ False

valid_rondo("A") ➞ False
Notes
Inputs will be given as all uppercase.
For the purposes of this challenge, accept ABA as valid Rondo forms.
"""

from unittest import TestCase


def valid_rondo(s):
    if len(s) < 3 or s[0] != 'A' or s[-1] != 'A':
        return False

    expected_char = 'B'
    for i in range(1, len(s) - 1, 2):
        if s[i] != expected_char or s[i + 1] != 'A':
            return False
        expected_char = chr(ord(expected_char) + 1)

    return True


TestCase().assertEqual(valid_rondo("ABACADAEAFAGAHAIAJA"), True)
TestCase().assertEqual(valid_rondo("ABA"), True)
TestCase().assertEqual(valid_rondo("ABBACCA"), False)
TestCase().assertEqual(valid_rondo("ACAC"), False)
TestCase().assertEqual(valid_rondo("A"), False)
TestCase().assertEqual(valid_rondo("AB"), False)
TestCase().assertEqual(valid_rondo("ABAC"), False)
TestCase().assertEqual(valid_rondo("ABACA"), True)
TestCase().assertEqual(valid_rondo("ABACADA"), True)
TestCase().assertEqual(valid_rondo("ABACADAEA"), True)
TestCase().assertEqual(valid_rondo("ABACADAEAFA"), True)
TestCase().assertEqual(valid_rondo("ABACADAEAFAGA"), True)
TestCase().assertEqual(valid_rondo("ABACADAEAFAGAHA"), True)
TestCase().assertEqual(valid_rondo("ABACADAEAFAGAHAIA"), True)
TestCase().assertEqual(valid_rondo("ABACADAEAFAGAHAIAJAKALAMANA"), True)
TestCase().assertEqual(valid_rondo("ABACADAEAAGAHAIAJAKALAMANA"), False)
TestCase().assertEqual(valid_rondo("ABACADAEAAGAHAIAJAKALAM"), False)
TestCase().assertEqual(valid_rondo("HELLO"), False)
