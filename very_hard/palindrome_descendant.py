"""
Palindrome Descendant

A number may not be a palindrome, but its descendant can be.
A number's direct child is created by summing each pair of adjacent digits to create the digits of the next number.

For instance, 123312 is not a palindrome, but its next child 363 is, where: 3 = 1 + 2; 6 = 3 + 3; 3 = 1 + 2.

Create a function that returns True if the number itself is a palindrome
or any of its descendants down to the first 2 digit number (a 1-digit number is trivially a palindrome).

Examples
palindrome_descendant(11211230) ➞ True
# 11211230 ➞ 2333 ➞ 56 ➞ 11

palindrome_descendant(13001120) ➞ True
# 13001120 ➞ 4022 ➞ 44

palindrome_descendant(23336014) ➞ True
# 23336014 ➞ 5665

palindrome_descendant(11) ➞ True
# Number itself is a palindrome
Notes
Numbers will always have an even number of digits.

"""


def palindrome_descendant(num):
    s_num = str(num)
    if len(s_num) == 1:
        return False

    if num == int(str(num)[::-1]):
        return True
    num = int("".join([str(int(s_num[i]) + int(s_num[i + 1])) for i in range(0, len(s_num) - 1, 2)]))
    return palindrome_descendant(num)


from unittest import TestCase

TestCase().assertEqual(palindrome_descendant(11211230), True)
TestCase().assertEqual(palindrome_descendant(13001120), True)
TestCase().assertEqual(palindrome_descendant(23336014), True)
TestCase().assertEqual(palindrome_descendant(11), True)
TestCase().assertEqual(palindrome_descendant(1122), False)
TestCase().assertEqual(palindrome_descendant(332233), True)
TestCase().assertEqual(palindrome_descendant(10210112), True)
TestCase().assertEqual(palindrome_descendant(9735), False)
TestCase().assertEqual(palindrome_descendant(97358817), False)
