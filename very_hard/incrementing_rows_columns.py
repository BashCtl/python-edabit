"""
Incrementing Rows and Columns


Write a function that takes in three parameters: r, c, i, where:

r and c are the number of rows and columns to initialize a zero matrix.
i represents the list of incrementing operations (+1).
And returns the resulting matrix after applying all the increment operations. Each increment operation will add 1 to the rows or columns specified in the incrementing list.

To illustrate:

final(3, 3, ["2r", "2c", "1r", "0c"])

# Initialize a 3 x 3 matrix of zeroes.

[
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]

# Apply "2r" (increment index 2 row).

[
  [0, 0, 0],
  [0, 0, 0],
  [1, 1, 1]
]

# Apply "2c" (increment index 2 column).

[
  [0, 0, 1],
  [0, 0, 1],
  [1, 1, 2]
]

# Apply "1r" (increment index 1 row).

[
  [0, 0, 1],
  [1, 1, 2],
  [1, 1, 2]
]

# Apply "0c" (increment index 0 column).
# This is the result you should return.

[
  [1, 0, 1],
  [2, 1, 2],
  [2, 1, 2]
]
Examples
final(2, 2, ["0r", "0r", "0r", "1c"]) ➞ [
  [3, 4],
  [0, 1]
]

final(2, 2, ["0c"]) ➞ [
  [1, 0],
  [1, 0]
]

final(3, 3, ["1c", "2c", "2c", "3c", "3c", "3c"]) ➞ [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]

final(3, 3, []) ➞ [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0]
]
Notes
The 2D matrix is 0-indexed.
The matrix created will have at least one row and one column.
All increment operations will be exactly +1.
"""
from unittest import  TestCase


def final(r, c, i):
    matrix = [[0 for _ in range(c)] for _ in range(r)]
    for operation in i:
        index, axis = int(operation[0]), operation[1]
        if axis == 'r':
            for col in range(c):
                matrix[index][col] += 1
        elif axis == 'c':
            for row in range(r):
                matrix[row][index] += 1

    return matrix




TestCase().assertEqual(final(2, 2, ['0r', '0r', '0r', '1c']), [
[3, 4], 
[0, 1]
])

TestCase().assertEqual(final(2, 2, ['0c']), [
[1, 0], 
[1, 0]
])

TestCase().assertEqual(final(3, 3, ['0c', '1c', '1c', '2c', '2c', '2c']), [
[1, 2, 3], 
[1, 2, 3], 
[1, 2, 3]
])

TestCase().assertEqual(final(3, 3, ["2r", "2c", "1r", "0c"]), [
[1, 0, 1], 
[2, 1, 2], 
[2, 1, 2]
])

TestCase().assertEqual(final(1, 1, []), [[0]])

TestCase().assertEqual(final(3, 3, ['0r', '2c', '1r', '2c', '1c', '1r', '1r']), [
[1, 2, 3], 
[3, 4, 5], 
[0, 1, 2]
])

TestCase().assertEqual(final(3, 3, []), [
[0, 0, 0], 
[0, 0, 0], 
[0, 0, 0]
])

TestCase().assertEqual(final(3, 4, ['1r', '1r', '1r', '3c', '3c', '3c']), [
[0, 0, 0, 3], 
[3, 3, 3, 6], 
[0, 0, 0, 3]
])

TestCase().assertEqual(final(10, 1, ['1r', '2r', '3r', '0c']), [
[1], 
[2], 
[2], 
[2], 
[1], 
[1], 
[1], 
[1], 
[1], 
[1]
])

TestCase().assertEqual(final(2, 5, ['1r', '1r', '1r', '1c', '0c', '0c', '1r', '0c', '1r', '0c']), [
[4, 1, 0, 0, 0], 
[9, 6, 5, 5, 5]
])