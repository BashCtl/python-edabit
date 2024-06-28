""""
Instances of the Fibonacci Sequence
Create a function that takes a number as an argument
and returns n instances of the Fibonacci sequence as a list.

Fibonacci numbers: F(n) = F(n-1) + F(n-2) with F(0) = 0 and F(1) = 1.
So the easy explanation is: The next element is the sum of the two previous elements.

If you want to read more about this sequence, take a look at the On-Line Encyclopedia
of Integer Sequences. Fibonacci numbers are strongly related to the golden ratio.
See the OEIS and Wikipedia links in the resources tab.

Examples
fib_seq(4) ➞ [0, 1, 1, 2]

fib_seq(7) ➞ [0, 1, 1, 2, 3, 5, 8]

fib_seq(0) ➞ []
Notes
If 0 is given, return an empty list.
If no argument is given, return None.
The input will never be a negative integer.

"""

from unittest import TestCase


def fib_seq(end=None):
    if end is None:
        return None
    x1, x2 = 0, 1
    result = []
    for _ in range(end):
        result.append(x1)
        x1, x2 = x2, x1 + x2
    return result


TestCase().assertEqual(fib_seq(2), [0, 1])
TestCase().assertEqual(fib_seq(4), [0, 1, 1, 2])
TestCase().assertEqual(fib_seq(0), [])
TestCase().assertEqual(fib_seq(7), [0, 1, 1, 2, 3, 5, 8])
TestCase().assertEqual(fib_seq(), None, 'An empty input has to return None')
TestCase().assertEqual(fib_seq(20),
                       [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181])
TestCase().assertEqual(fib_seq(1), [0])
