"""
N-Length Letter Groups

Write a function that returns a list of strings populated from the slices
of n-length characters of the given word (a slice after another while n-length applies onto the word).

Examples
collect("intercontinentalisationalism", 6)
➞ ["ationa", "interc", "ntalis", "ontine"]

collect("strengths", 3)
➞ ["eng", "str", "ths"]

collect("pneumonoultramicroscopicsilicovolcanoconiosis", 15)
➞ ["croscopicsilico", "pneumonoultrami", "volcanoconiosis"]

Notes
Ensure that the resulting array is lexicographically ordered.
Return an empty array if the given string is less than n.
"""
import textwrap


def collect(s, n):
    if len(s) >= n:
        return sorted([chunk for chunk in textwrap.wrap(s, n) if len(chunk) == n])
    else:
        return []


print(collect("intercontinentalisationalism", 6))
