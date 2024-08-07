"""
Double Palindromes
Strings can be segregated into both their letter and digit components.

A double palindrome is when a string's letter component and digit component are both palindromes.
A single-palindrome is when either (but not both) the letter component or the digit component are palindromes.
To illustrate:

"cab97ac79"
# double-palindrome: "cabac" and "9779" are both palindromes.

"1abc4de1"
# single-palindrome: "141" is a palindrome.
Write a function that maps double palindromes to the number 2, single palindromes to the number 1, and everything else to the number 0.

Examples
palindrome_set(["cb77c", "ccc888", "ccc789", "abc89"]) ➞ [2, 2, 1, 0]

palindrome_set(["789", "555", "ccc", "abba"]) ➞ [0, 1, 1, 1]

palindrome_set(["7a", "5f", "6c"]) ➞ [2, 2, 2]
Notes
A string is composed of only letters or only numbers, can be at most a single palindrome (see example #2).
All single character components are trivially palindromes (see example #3).
All letters will be lower cased.

"""

from unittest import TestCase


def is_palindrome(s):
    return s == s[::-1]


def palindrome_set(lst):
    results = []
    for s in lst:
        letters = ''.join([char for char in s if char.isalpha()])
        digits = ''.join([char for char in s if char.isdigit()])

        letters_palindrome = is_palindrome(letters) if letters else False
        digits_palindrome = is_palindrome(digits) if digits else False

        if letters_palindrome and digits_palindrome:
            results.append(2)
        elif letters_palindrome or digits_palindrome:
            results.append(1)
        else:
            results.append(0)
    return results


TestCase().assertEqual(palindrome_set(["cb77c", "ccc888", "ccc789", "abc89"]), [2, 2, 1, 0])
TestCase().assertEqual(palindrome_set(["18a99b89cc881ba", "p7o8p987", "p7o", "p7o8"]), [1, 2, 1, 0])
TestCase().assertEqual(palindrome_set(["ab9a", "abba", "aa78bb8bbaa7", "a88a"]), [2, 1, 2, 2])
TestCase().assertEqual(palindrome_set(["789", "555", "ccc", "abba"]), [0, 1, 1, 1])
TestCase().assertEqual(palindrome_set(["7a", "5f", "6c"]), [2, 2, 2])
TestCase().assertEqual(palindrome_set(["7ab", "5fc", "6cd"]), [1, 1, 1])
TestCase().assertEqual(palindrome_set(["87ab", "15fc", "26cd"]), [0, 0, 0])
TestCase().assertEqual(palindrome_set(["1234ab", "144a441"]), [0, 2])
TestCase().assertEqual(palindrome_set([""]), [0])
