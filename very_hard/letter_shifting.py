"""
Letter Shifting

Create a function that takes a string and shifts the letters to the right by an amount n but not the whitespace.

Examples
shift_letters("Boom", 2) ➞ "omBo"

shift_letters("This is a test",  4) ➞ "test Th i sisa"

shift_letters("A B C D E F G H", 5) ➞  "D E F G H A B C"
Notes
Keep the case as it is.
n can be larger than the total number of letters


"""
import re
from collections import deque


def shift_letters(txt, n):
    space_indexes = [i for i, char in enumerate(txt) if char == ' ']
    txt = re.sub(" ", "", txt)
    lst = deque(txt)
    lst.rotate(n)
    lst = list(lst)
    for i in space_indexes:
        lst.insert(i, " ")
    return "".join(lst)


print(shift_letters("A B C D E F G H", 5))
print(shift_letters("Edabit helps you learn in bitesize chunks", 39))