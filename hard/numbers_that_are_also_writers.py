"""
Numbers That are Also Writers

If a number is autobiographical, then the number's digits describe itself.
The first digit is the amount of times the digit 0 appears,
the second digit is the amount of times the digit 1 appears,
the third digit is the amount of times the digit 2 appears, etc.
This repeats for all digits of the number. The number 6210001000 is autobiographical,
because it has six 0's, two 1's, one 2, zero 3's, zero 4's, zero 5's, one 6, zero 7's, zero 8's, and zero 9's.

Create a function that takes an integer n and returns whether or not n is an autobiographical number.

Examples
is_autobiographical(6210001000) ➞ True

is_autobiographical(12345) ➞ False

is_autobiographical(1210) ➞ True
# one 0, two 1's, one 2, zero 3's

is_autobiographical(638) ➞ False

is_autobiographical(0) ➞ False
# claims no zeroes, however zero is the first digit

Notes
Numbers with more than 10 digits should always return False
(9 is the highest digit in base 10, so you can't go higher than 9,999,999,999).
n is always >= 0 and is always an integer.
"""


def is_autobiographical(n):
    num = str(n)
    if len(num) > 10:
        return False
    for i, v in enumerate(num):
        if num.count(str(i)) != int(v):
            return False
    return True


print(is_autobiographical(6210001000))
print(is_autobiographical(12345))
print(is_autobiographical(1210))
print(is_autobiographical(638))
print(is_autobiographical(0))