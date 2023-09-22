"""
Sort Characters by Frequency, Case, Alphabet
The function is given a string. Sort the characters and return a new string. Sorting conditions:

Most frequent (case-specific) move in front.
For the same frequency upper case characters move in front.
For the same frequency and case sort them alphabetically.

Examples

frequency_sort("tree") ➞ "eert"

frequency_sort("cccaaa") ➞ "aaaccc"

frequency_sort("Aabb") ➞ "bbAa"
"""


def frequency_sort(s):
    func = lambda a: (-s.count(a), a.islower(), a)
    return "".join(sorted(s, key=func))


print(frequency_sort("tree"))
print(frequency_sort("cccaaa"))
print(frequency_sort("Aabb"))
