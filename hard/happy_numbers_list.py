from unittest import TestCase

"""
Happy Numbers

You are given a list of 0s and 1s, like the one below:

[0, 1, 0, 0, 0, 1, 1, 1, 0, 1]

# The first element, a 0, and the last element, a 1 are both unhappy.
# The second element, a 1 is unhappy.
# The second-to-last element, a 0 is unhappy.
# All other numbers in this list are happy.
A 1 is unhappy if the digit to its left 
and the digit to its right are both 0s. A 0 is unhappy if the digit to its left 
and the digit to its right are both 1s. If a number has only one neighbor, 
it is unhappy if its only neighbor is different. Otherwise, a number is happy.

Write a function that takes in a list of 0s and 1s 
and outputs the portion of numbers which are happy. 
The total portion of numbers which are happy can be represented as:

portion of happy numbers = (happy 0s + happy 1s) / total numbers
In the example above, 0.6 is the number of happy numbers.

Examples
portion_happy([0, 1, 0, 1, 0]) ➞ 0

portion_happy([0, 1, 1, 0]) ➞ 0.5

portion_happy([0, 0, 0, 1, 1]) ➞ 1

portion_happy([1, 0, 0, 1, 1]) ➞ 0.8

Notes
Remember: a 0 border number is unhappy if its only neighbor is a 1 and vice versa.
A list will contain at least two elements.

"""


def portion_happy(numbers):
    count = 0
    for i in range(1, len(numbers) - 1):
        if numbers[i] == numbers[i - 1] or numbers[i] == numbers[i + 1]:
            count += 1
    if numbers[0] == numbers[1]:
        count += 1
    if numbers[-1] == numbers[-2]:
        count += 1
    return count / len(numbers)


TestCase().assertEqual(portion_happy([0, 1, 0, 1, 0]), 0)
TestCase().assertEqual(portion_happy([0, 1, 1, 0]), 0.5)
TestCase().assertEqual(portion_happy([0, 0, 0, 1, 1]), 1)
TestCase().assertEqual(portion_happy([1, 0, 0, 1, 1]), 0.8)
TestCase().assertEqual(portion_happy([1, 1, 1, 1, 1]), 1)
TestCase().assertEqual(portion_happy([1, 1, 0, 0, 1, 1]), 1)
TestCase().assertEqual(portion_happy([1, 1, 0, 0, 0, 1, 1]), 1)
TestCase().assertEqual(portion_happy([1, 0, 0, 0, 1]), 0.6)
TestCase().assertEqual(portion_happy([1, 0, 1, 0, 0, 0]), 0.5)
TestCase().assertEqual(portion_happy([1, 1]), 1)
TestCase().assertEqual(portion_happy([1, 0]), 0)
