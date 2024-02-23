"""
Recursion: Fibonacci Word

A Fibonacci word is a specific sequence of binary digits (or symbols from any two-letter alphabet).
The Fibonacci word is formed via repeated concatenation in the same fashion
that the Fibonacci numbers are formed via repeated addition.

Create a function that takes a number n as an argument
and returns the first n elements of the Fibonacci word sequence.

Examples
generate_word(1) ➞ "invalid"
# if n < 2 then return "invalid".

generate_word(3) ➞ "b, a, ab"

generate_word(7) ➞ "b, a, ab, aba, abaab, abaababa, abaababaabaab"
Notes
You are expected to solve this challenge via recursion.

"""


def generate_word(n, letters=[]):
    if n < 2 and len(letters) == 0:
        return "invalid"

    if n == 0:
        result = ", ".join(letters)
        letters.clear()
        return result

    if len(letters) == 0:
        letters.append("b")
        letters.append("a")
        n -= 2
    l = len(letters)
    letters.append(letters[l - 2] + letters[l - 1])
    return generate_word(n - 1, letters)


print(generate_word(3))
print(generate_word(7))
