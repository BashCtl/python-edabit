from unittest import TestCase

"""
The Magic Square Game

There are two players, Alice and Bob, each with a 3-by-3 grid. 
A referee tells Alice to fill out one particular row in the grid 
(say the second row) by putting either a 1 or a 0 in each box, 
such that the sum of the numbers in that row is odd. 
The referee tells Bob to fill out one column in the grid 
(say the first column) by putting either a 1 or a 0 in each box, 
such that the sum of the numbers in that column is even.

Alice and Bob win the game if Alice’s numbers give an odd sum, 
Bob’s give an even sum, and (most important) they’ve each written down the same number 
in the one square where their row and column intersect.

Examples
magic_square_game([2, "100"], [1, "101"]) ➞ False

magic_square_game([2, "001"], [1, "101"]) ➞ True

magic_square_game([3, "111"], [2, "011"]) ➞ True

magic_square_game([1, "010"], [3, "101"]) ➞ False

# Two lists, Alice [row, "her choice"], Bob [column, "his choice"]

Notes

The row of Alice is always odd, the column of Bob is always even.

"""


def magic_square_game(alice, bob):
    column = alice[0] - 1
    row = bob[0] - 1
    alice_sum = sum([int(i) for i in alice[1]])
    bob_sum = sum([int(i) for i in bob[1]])
    return alice_sum % 2 == 1 and bob_sum % 2 == 0 and alice[1][row] == bob[1][column]


TestCase().assertEqual(magic_square_game([2, '100'], [1, '101']), False)
TestCase().assertEqual(magic_square_game([2, '001'], [1, '101']), True)
TestCase().assertEqual(magic_square_game([3, '111'], [2, '011']), True)
TestCase().assertEqual(magic_square_game([1, '010'], [3, '101']), False)
TestCase().assertEqual(magic_square_game([2, '111'], [3, '011']), True)
TestCase().assertEqual(magic_square_game([2, '100'], [3, '110']), False)
TestCase().assertEqual(magic_square_game([1, '001'], [1, '101']), False)
TestCase().assertEqual(magic_square_game([2, '100'], [2, '101']), True)
TestCase().assertEqual(magic_square_game([3, '010'], [1, '110']), True)
TestCase().assertEqual(magic_square_game([1, '100'], [2, '110']), False)
TestCase().assertEqual(magic_square_game([2, '111'], [3, '011']), True)
TestCase().assertEqual(magic_square_game([2, '001'], [2, '101']), True)
TestCase().assertEqual(magic_square_game([1, '100'], [2, '101']), False)
TestCase().assertEqual(magic_square_game([3, '001'], [3, '011']), True)
TestCase().assertEqual(magic_square_game([3, '111'], [1, '110']), False)
TestCase().assertEqual(magic_square_game([2, '100'], [2, '101']), True)
