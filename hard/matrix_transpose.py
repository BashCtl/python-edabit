"""
Matrix Transpose

Create a function that transposes a 2D matrix.

Examples
transpose_matrix([
  [1, 1, 1],
  [2, 2, 2],
  [3, 3, 3]
]) ➞ [
  [1, 2, 3],
  [1, 2, 3],
  [1, 2, 3]
]

transpose_matrix([
  [5, 5],
  [6, 7],
  [9, 1]
]) ➞ [
  [5, 6, 9],
  [5, 7, 1]
]

"""


def transpose_matrix(lst):
    return [[lst[j][i] for j in range(len(lst))] for i in range(len(lst[0]))]


print(transpose_matrix([
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]))
