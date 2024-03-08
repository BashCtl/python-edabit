"""
Vertical Text

Create a function that converts a string into a matrix of characters that
can be read vertically. Add spaces when characters are missing.

Examples
vertical_txt("Holy bananas") ➞ [
  ["H", "b"],
  ["o", "a"],
  ["l", "n"],
  ["y", "a"],
  [" ", "n"],
  [" ", "a"],
  [" ", "s"]
]

vertical_txt("Hello fellas") ➞ [
  ["H", "f"],
  ["e", "e"],
  ["l", "l"],
  ["l", "l"],
  ["o", "a"],
  [" ", "s"]
]

"""


def vertical_txt(txt):
    words = txt.split()

    max_length = max(len(word) for word in words)

    matrix = [[" " for _ in range(len(words))] for _ in range(max_length)]

    for i, word in enumerate(words):
        for j, char in enumerate(word):
            matrix[j][i] = char

    return matrix
