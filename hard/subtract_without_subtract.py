"""
Subtract Without Subtract

Create a function that subtracts one positive integer from another,
without using any arithmetic operators such as -, %, /, +, etc.

Examples
my_sub(5, 9) ➞ 4

my_sub(10, 30) ➞ 20

my_sub(0, 0) ➞ 0
Notes
Do not multiply by -1.
Use bitwise operations only: <<, |, ~, &, etc.

"""


def my_sub(a, b):
    while a != 0:
        borrow = (~b) & a
        b = b ^ a
        a = borrow << 1
    return b


print(my_sub(5, 9))
