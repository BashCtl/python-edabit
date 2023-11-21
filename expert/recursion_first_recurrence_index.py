"""
Recursion: First Recurrence Index

Create a recursive function that identifies the very first item
that has recurred in the string argument passed.
It returns the identified item with the index where it first appeared
and the very next index where it resurfaced - entirely as an object;
or an empty object if the passed argument is either None,
an empty string, or no recurring item exists.

Examples
recur_index("KDXTDATTDD") ➞ {"D": [1, 4]}
// D first appeared at index 1, resurfaced at index 4
//  though D resurfaced yet again at index 8, it's no longer significant
// T appeared and resurfaced at indices 3 and 6 but D completed the cycle first

recur_index("AKEDCBERSD") ➞ {"E": [2, 6]}

recur_index("DXKETRETXD") ➞ {"E": [3, 6]}

recur_index("ABCKPEPGBC") ➞ {"P": [4, 6]}

recur_index("ABCDEFGHIJ") ➞ {}

recur_index(None) ➞ {}

Notes
There will be no exceptions to handle, all inputs are strings
and string-like objects. You just need to be extra careful on None,
and empty string inputs to avoid undesirable results.

It is expected from the challenge-takers to come up with a solution
using the concept of recursion or the so-called recursive approach.

"""

def recur_index(txt, i=0, result={}):
    if txt is None or len(txt) == 0:
        return result
    if i == len(txt):
        if not result:
            return result
        key, value = min(result.items(), key=lambda x: (x[1][1], x[1][0]))
        result.clear()
        return {key: value}
    k = txt[i]
    indexes = [ind for ind, c in enumerate(txt) if c == k]
    indexes = indexes[:2]
    if len(indexes) == 2:
        result[k] = indexes

    return recur_index(txt, i + 1, result)


print(recur_index("KDXTDATTDD"))
print("-" * 20)
print(recur_index("DXKETRETXD"))
print("-" * 20)
print(recur_index("ABCKPEPGBC"))
print("-" * 20)
print(recur_index("ABCDEFGHIJ"))
print("-" * 20)
