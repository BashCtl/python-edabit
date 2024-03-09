"""
Staircase of Recursion

Write a function that returns the number of ways a person can climb n stairs, where the person may only climb 1 or 2 steps at a time.

To illustrate, if n = 4 there are 5 ways to climb:

[1, 1, 1, 1]
[2, 1, 1]
[1, 2, 1]
[1, 1, 2]
[2, 2]
Examples
ways_to_climb(1) ➞ 1

ways_to_climb(2) ➞ 2

ways_to_climb(5) ➞ 8
Notes
A staircase of height 0 should return 1.


"""


def ways_to_climb(n, fib=[]):
    if n <= 1 and len(fib) == 0:
        return 1
    if len(fib) == 0:
        fib.append(0)
        fib.append(1)

    if n == 0:
        result = fib[-1]
        fib.clear()
        return result
    fib.append(fib[len(fib) - 1] + fib[len(fib) - 2])
    n -= 1
    return ways_to_climb(n, fib)


print(ways_to_climb(5))

