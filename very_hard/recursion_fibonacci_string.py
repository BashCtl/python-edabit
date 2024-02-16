"""
Recursion: Fibonacci String


A Fibonacci string is a precedence of the Fibonacci series.
It works with any two characters of the English alphabet
(as opposed to the numbers 0 and 1 in the Fibonacci series)
as the initial items and concatenates them together
as it progresses similarly to that of the Fibonacci series.

Examples
fib_str(3, ["j", "h"]) ➞ "j, h, hj"

fib_str(5, ["e", "a"]) ➞ "e, a, ae, aea, aeaae"

fib_str(6, ["n", "k"]) ➞ "n, k, kn, knk, knkkn, knkknknk"

Notes
All values for n will be at least 2.
It is expected from the challenge-takers to come up with
a solution using the concept of recursion or the so-called recursive approach.

"""


def fib_str(n, f):
    if n == 2:
        return ", ".join(f)
    f.append(f[len(f) - 1] + f[len(f) - 2])
    return fib_str(n - 1, f)


print(fib_str(3, ["j", "h"]))
print(fib_str(5, ["e", "a"]))
