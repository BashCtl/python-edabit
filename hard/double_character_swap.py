"""
Double Character Swap

Write a function to replace all instances of character c1 with character c2 and vice versa.

Examples
double_swap( "aabbccc", "a", "b") ➞ "bbaaccc"

double_swap("random w#rds writt&n h&r&", "#", "&")
➞ "random w&rds writt#n h#r#"

double_swap("128 895 556 788 999", "8", "9")
➞ "129 985 556 799 888"
Notes
Both characters will show up at least once in the string.

"""
from unittest import TestCase


def double_swap(text, c1, c2):
    result = []
    for char in text:
        if char == c1:
            result.append(c2)
        elif char == c2:
            result.append(c1)
        else:
            result.append(char)
    return ''.join(result)





TestCase().assertEqual(double_swap("aabbccc", "a", "b"), "bbaaccc")
TestCase().assertEqual(double_swap("random w#rds writt&n h&r&", "#", "&"), "random w&rds writt#n h#r#")
TestCase().assertEqual(double_swap("128 895 556 788 999", "8", "9"), "129 985 556 799 888")
TestCase().assertEqual(double_swap("mamma mia", "m", "a"), "amaam aim")
TestCase().assertEqual(double_swap("**##**", "*", "#"), "##**##")
TestCase().assertEqual(double_swap("123456789", "4", "5"), "123546789")
TestCase().assertEqual(double_swap("445566&&", "4", "&"), "&&556644")
TestCase().assertEqual(double_swap("!?@,.", ",", "."), "!?@.,")
TestCase().assertEqual(double_swap("Q_Q T_T =.= >.<", "Q", "T"), "T_T Q_Q =.= >.<")
TestCase().assertEqual(double_swap("(Q_Q) (T_T) (=.=) (>.<)", ")", "("), ")Q_Q( )T_T( )=.=( )>.<(")
TestCase().assertEqual(double_swap("<>", ">", "<"), "><")
TestCase().assertEqual(double_swap("001101", "1", "0"), "110010")
TestCase().assertEqual(double_swap("!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~", "a", "b"), "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`bacdefghijklmnopqrstuvwxyz{|}~")