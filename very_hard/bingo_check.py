"""
Bingo Check
Create a function that takes a 5x5 2D list
and returns True if it has at least one Bingo, and False if it doesn't.

Examples
bingo_check([
  [45, "x", 31, 74, 87],
  [64, "x", 47, 32, 90],
  [37, "x", 68, 83, 54],
  [67, "x", 98, 39, 44],
  [21, "x", 24, 30, 52]
]) ➞ True

bingo_check([
  ["x", 43, 31, 74, 87],
  [64, "x", 47, 32, 90],
  [37, 65, "x", 83, 54],
  [67, 98, 39, "x", 44],
  [21, 59, 24, 30, "x"]
]) ➞ True

bingo_check([
  ["x", "x", "x", "x", "x"],
  [64, 12, 47, 32, 90],
  [37, 16, 68, 83, 54],
  [67, 19, 98, 39, 44],
  [21, 75, 24, 30, 52]
]) ➞ True

bingo_check([
  [45, "x", 31, 74, 87],
  [64, 78, 47, "x", 90],
  [37, "x", 68, 83, 54],
  [67, "x", 98, "x", 44],
  [21, "x", 24, 30, 52]
]) ➞ False
Notes
Only check for diagonals, horizontals and verticals.
"""


def bingo_check(board):
    for row in board:
        if all(cell == "x" for cell in row):
            return True

    for col in range(5):
        if all(row[col] == "x" for row in board):
            return True

    if all(board[i][i] == "x" for i in range(5)):
        return True

    if all(board[i][4 - i] == "x" for i in range(5)):
        return True

    return False


from unittest import TestCase

TestCase().assertEqual(bingo_check([
    [45, "x", 31, 74, 87],
    [64, "x", 47, 32, 90],
    [37, "x", 68, 83, 54],
    [67, "x", 98, 39, 44],
    [21, "x", 24, 30, 52]
]), True)

TestCase().assertEqual(bingo_check([
    ["x", 43, 31, 74, 87],
    [64, "x", 47, 32, 90],
    [37, 65, "x", 83, 54],
    [67, 98, 39, "x", 44],
    [21, 59, 24, 30, "x"]
]), True)

TestCase().assertEqual(bingo_check([
    [37, 16, 84, 51, 33],
    [64, 12, 47, 32, 90],
    ["x", "x", "x", "x", "x"],
    [67, 19, 98, 39, 44],
    [21, 75, 24, 30, 52]
]), True)

TestCase().assertEqual(bingo_check([
    [45, "x", 31, 74, 87],
    [64, 78, "x", "x", 90],
    [37, "x", 68, "x", 54],
    [67, "x", 98, "x", "x"],
    [21, "x", 24, 30, 52]
]), False)

TestCase().assertEqual(bingo_check([
    [45, 46, 31, 74, "x"],
    [64, 78, 80, "x", 90],
    [37, 81, "x", 55, 54],
    [67, "x", 98, 34, 77],
    ["x", 33, 24, 30, 52]
]), True)
