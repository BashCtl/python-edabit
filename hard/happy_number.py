"""
Happy Number


A happy number is a number which yields a 1 by repeatedly summing up
the square of its digits. If such a process results in an endless
cycle of numbers containing 4, the number is said to be an unhappy number.

Create a function that accepts a number and determines whether the number
is a happy number or not. Return True if so, False otherwise.

Examples
is_happy(67) ➞ False

is_happy(89) ➞ False

is_happy(139) ➞ True

is_happy(1327) ➞ False

is_happy(2871) ➞ False

is_happy(3970) ➞ True

Notes
Hint: Your loop terminates if the value of n is either 1 or 4.
Alternatively, you can solve this challenge via a recursive approach.
"""


def is_happy(n):
    if n == 4:
        return False
    if n == 1:
        return True
    n = sum([int(x) ** 2 for x in str(n)])

    return is_happy(n)


print(is_happy(67))
print(is_happy(89))
print(is_happy(139))