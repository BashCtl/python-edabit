"""
Longest Common Ending


Write a function that returns the longest common ending between two strings.

Examples
longest_common_ending("multiplication", "ration") ➞ "ation"

longest_common_ending("potent", "tent") ➞ "tent"

longest_common_ending("skyscraper", "carnivore") ➞ ""
Notes
Return an empty string if there exists no common ending.

"""

from unittest import TestCase


def longest_common_ending(txt1, txt2):
    l = min(len(txt1), len(txt2))
    result = []
    for i in range(1, l + 1):
        if txt1[-i] == txt2[-i]:
            result.insert(0, txt1[-i])
        else:
            break

    return "".join(result) if result else ""


TestCase().assertEqual(longest_common_ending("pitiful", "beautiful"), "tiful")
TestCase().assertEqual(longest_common_ending("truck", "trick"), "ck")
TestCase().assertEqual(longest_common_ending("vote", "asymptote"), "ote")
TestCase().assertEqual(longest_common_ending("multiplication", "ration"), "ation")
TestCase().assertEqual(longest_common_ending("potent", "tent"), "tent")
TestCase().assertEqual(longest_common_ending("skyscraper", "carnivore"), "")
