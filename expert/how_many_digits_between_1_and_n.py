"""
How Many Digits between 1 and N

Imagine you took all the numbers between 0 and n and concatenated
them together into a long string. How many digits are there between 0 and n?
Write a function that can calculate this.

There are 0 digits between 0 and 1, there are 9 digits between 0 and 10
and there are 189 digits between 0 and 100.

Examples
digits(1) ➞ 0

digits(10) ➞ 9

digits(100) ➞ 189

digits(2020) ➞ 6969

Notes
The numbers are going to be rather big so creating that string won't be practical.

"""


def digits(number):
    l = len(str(number)) - 1
    result = l * 10 ** l + (1 - 10 ** l) // 9
    result += (number - 10 ** l) * len(str(10 ** l))
    return result


print(digits(1))
print(digits(10))
print(digits(100))
print(digits(2020))
