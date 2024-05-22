"""
Layers in a Rug

Write a function that counts how many concentric layers a rug has.

Examples
count_layers([
  "AAAA",
  "ABBA",
  "AAAA"
]) ➞ 2

count_layers([
  "AAAAAAAAA",
  "ABBBBBBBA",
  "ABBAAABBA",
  "ABBBBBBBA",
  "AAAAAAAAA"
]) ➞ 3

count_layers([
  "AAAAAAAAAAA",
  "AABBBBBBBAA",
  "AABCCCCCBAA",
  "AABCAAACBAA",
  "AABCADACBAA",
  "AABCAAACBAA",
  "AABCCCCCBAA",
  "AABBBBBBBAA",
  "AAAAAAAAAAA"
]) ➞ 5
Notes
Multiple layers can share the same component so count them separately (example #2).
Layers will be horizontally and vertically symmetric.
There will be at least one layer for each rug.
"""

from unittest import TestCase


def count_layers(rug):
    n = len(rug)
    unique_layers = set()
    for i in range((n + 1) // 2):
        unique_layers.add(rug[i])

    return len(unique_layers)


TestCase().assertEqual(count_layers([
    "AAA"]), 1)

TestCase().assertEqual(count_layers([
    "AAAA",
    "AAAA",
    "AAAA"]), 1)

TestCase().assertEqual(count_layers([
    "AAAA",
    "ABBA",
    "AAAA"]), 2)

TestCase().assertEqual(count_layers([
    "AAAAAAAAA",
    "ABBBBBBBA",
    "ABBBBBBBA",
    "ABBBBBBBA",
    "AAAAAAAAA"]), 2)

TestCase().assertEqual(count_layers([
    "AAAAAAAAA",
    "ABBBBBBBA",
    "ABBAAABBA",
    "ABBBBBBBA",
    "AAAAAAAAA"]), 3)

TestCase().assertEqual(count_layers([
    "AAAAAAAAA",
    "ABBBBBBBA",
    "ABCCCCCBA",
    "ABBBBBBBA",
    "AAAAAAAAA"]), 3)

TestCase().assertEqual(count_layers([
    "AAAAAAAAAAA",
    "AABBBBBBBAA",
    "AABCCCCCBAA",
    "AABCAAACBAA",
    "AABCADACBAA",
    "AABCAAACBAA",
    "AABCCCCCBAA",
    "AABBBBBBBAA",
    "AAAAAAAAAAA"]), 5)

TestCase().assertEqual(count_layers([
    "AAAAAAAAAAA",
    "AABBBBBBBAA",
    "AABCCCCCBAA",
    "AABCAAACBAA",
    "AABCABACBAA",
    "AABCAAACBAA",
    "AABCCCCCBAA",
    "AABBBBBBBAA",
    "AAAAAAAAAAA"]), 5)

TestCase().assertEqual(count_layers([
    "AAAAAAAAAAA",
    "AABBBBBBBAA",
    "AABCCCCCBAA",
    "AABCDDDCBAA",
    "AABCDDDCBAA",
    "AABCDDDCBAA",
    "AABCCCCCBAA",
    "AABBBBBBBAA",
    "AAAAAAAAAAA"]), 4)

TestCase().assertEqual(count_layers([
    "FFFFFFFFFFFFFFFFFFFFFFFFF",
    "FFFFFFFFFFFFFFFFFFFFFFFFF",
    "FFFFGGGGGGGGGGGGGGGGGFFFF",
    "FFFFGGGAAAAAAAAAAAGGGFFFF",
    "FFFFGGGAABBBBBBBAAGGGFFFF",
    "FFFFGGGAABCCCCCBAAGGGFFFF",
    "FFFFGGGAABCDDDCBAAGGGFFFF",
    "FFFFGGGAABCDDDCBAAGGGFFFF",
    "FFFFGGGAABCDDDCBAAGGGFFFF",
    "FFFFGGGAABCCCCCBAAGGGFFFF",
    "FFFFGGGAABBBBBBBAAGGGFFFF",
    "FFFFGGGAAAAAAAAAAAGGGFFFF",
    "FFFFGGGGGGGGGGGGGGGGGFFFF",
    "FFFFFFFFFFFFFFFFFFFFFFFFF",
    "FFFFFFFFFFFFFFFFFFFFFFFFF"]), 6)
