"""
Maximize the First Number
Write a function that makes the first number as
large as possible by swapping out its digits for digits in the second number.
To illustrate:

max_possible(9328, 456) ➞ 9658
# 9658 is the largest possible number built from swaps from 456.
# 3 replaced with 6 and 2 replaced with 5.
Examples
max_possible(523, 76) ➞ 763

max_possible(9132, 5564) ➞ 9655

Notes
Each digit in the second number can only be used once.
Zero to all digits in the second number may be used.

"""


def max_possible(n1, n2):
    ns1 = [i for i in str(n1)]
    ns2 = sorted(str(n2), reverse=True)
    for n in ns2:
        for i in range(len(ns1)):
            if int(n)> int(ns1[i]):
                ns1[i]=n
                break

    return int("".join(ns1))


print(max_possible(9328, 456))
print(max_possible(9132, 5564))
print(max_possible(8732, 91255))
