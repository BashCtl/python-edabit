"""
Ice Cream Sandwich

An ice cream sandwich is a string that is formed by two identical ends and a different middle.

Some examples of ice cream sandwiches:
"AABBBAA"

"3&&3"

"yyyyymmmmmmmmyyyyy"

"hhhhhhhhmhhhhhhhh"
Notice how left and right ends of the sandwich are identical in both length and in repeating character). The middle section is distinctly different.

Not ice cream sandwiches:
"BBBBB"
// You can't have just plain icecream.

"AAACCCAA"
// You can't have unequal sandwich ends.

"AACDCAA"
// You can't have more than one filling.

"A"
// You can't have fewer than 3 characters.
Write a function that returns True if a string is an ice cream sandwich and False otherwise.

Examples
is_icecream_sandwich("CDC") ➞ True

is_icecream_sandwich("AAABB") ➞ False

is_icecream_sandwich("AA") ➞ False
Notes
An ice cream sandwich must have a minimum length of 3 characters, and at least two of these characters must be distinct (you can't only have the filling!).
"""

from unittest import TestCase


def is_icecream_sandwich(s):
    n = len(s)
    if n < 3:
        return False

    left_char = s[0]
    left_length = 0
    while left_length < n and s[left_length] == left_char:
        left_length += 1

    right_char = s[-1]
    right_length = 0
    while right_length < n and s[-(right_length + 1)] == right_char:
        right_length += 1

    if left_length != right_length or left_char != right_char:
        return False

    middle = s[left_length:n - right_length]
    if not middle or middle == left_char or len(set(middle)) > 1:
        return False

    return True


TestCase().assertEqual(is_icecream_sandwich(""), False, "too short")
TestCase().assertEqual(is_icecream_sandwich("AABBBAA"), True)
TestCase().assertEqual(is_icecream_sandwich("3&&3"), True)
TestCase().assertEqual(is_icecream_sandwich("yyyyymmmmmmmmyyyyy"), True)
TestCase().assertEqual(is_icecream_sandwich("hhhhhhhhmhhhhhhhh"), True)
TestCase().assertEqual(is_icecream_sandwich("CDC"), True)
TestCase().assertEqual(is_icecream_sandwich("BBBBB"), False, "only filling")
TestCase().assertEqual(is_icecream_sandwich("AAACCCAA"), False, "ends are unbalanced")
TestCase().assertEqual(is_icecream_sandwich("AACDCAA"), False, "can only have one type of filling")
TestCase().assertEqual(is_icecream_sandwich("AAABB"), False, "only one end")
TestCase().assertEqual(is_icecream_sandwich("AA"), False, "too short")
TestCase().assertEqual(is_icecream_sandwich("A"), False, "too short")
