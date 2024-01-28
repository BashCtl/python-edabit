"""
Maximum Occurrence

Given a string text. Write a function that returns the character with
the highest frequency. If more than 1 character has the same highest frequency,
return all those characters as an array sorted in ascending order.
If there is no repetition in characters, return "No Repetition".

Examples
max_occur("Computer Science") ➞ ['e']

max_occur("Edabit") ➞ "No Repetition"

max_occur("system admin") ➞ ['m', 's']

max_occur("the quick brown fox jumps over the lazy dog") ➞ [' ']

Notes
Try to make use of the concept used in counting sort.

"""


def max_occur(text):
    max_occurrence = max([text.count(l) for l in set(text)])
    return sorted([c for c in set(text) if text.count(c) == max_occurrence]) if max_occurrence > 1 else "No Repetition"


print(max_occur("system admin"))
print(max_occur("Edabit"))
