"""
Recursion: Reversed List Index

Write a recursive function that filters the items in a list (given as parameter arr)
by positional parity (odd or even), given as parameter par, starting from the opposite end.
Return a list of items on odd positions (... 5, 3, 1) or on even positions (... 6, 4, 2)
and counting from the last item in the list.

Examples
get_items_at([2, 4, 6, 8, 10], "odd") ➞ [2, 6, 10]
// 2, 6 & 10 occupy the 5th, 3rd and 1st positions from right.
// Odd positions, hence the parity, and from the opposite.

get_items_at(["E", "D", "A", "B", "I", "T"], "even") ➞ ["E", "A", "I"]
// E, A and I occupy the 6th, 4th and 2nd positions from right.
// Even positions, hence the parity, and from the opposite.

get_items_at([")", "(", "*", "&", "^", "%", "$", "#", "@", "!"], "even") ➞ [")", "*", ^", "$", "@"]

get_items_at(["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"], "even") ➞ ["R", "I", "R", "R", "L"]


Notes
IMPORTANT: You are advised to solve this challenge via a recursive approach, hence,
the very purpose of this challenge. You can check the Resources tab about a few topics on recursion.
Lists are zero-indexed, so, index+1 = position or position-1 = index.
Items in the list may contain duplicates. See example #4.
The last item in the list is always the first item to start a positional count.
The sequence of the items in the resulting list should be retained
(i.e. example #1 - 6 should come after 2 and before 10, example #2 - "A" should come after "E"
and before "I").

"""


def get_items(arr, par, index):
    if len(arr) == 0 or index >= len(arr):
        return []
    odr_or_even = 0 if par == "even" else 1
    if (len(arr) - index) & 1 == odr_or_even:
        return [arr[index]] + get_items(arr, par, index + 1)
    else:
        return get_items(arr, par, index + 1)


def get_items_at(arr, par):
    return get_items(arr, par, 0)


# print(get_items_at([2, 4, 6, 8, 10], "odd"))
# print(get_items_at(["E", "D", "A", "B", "I", "T"], "even"))
# print(get_items_at( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], "odd"))
# print(get_items_at([2, 4, 6, 8, 10], "even"))

exp_vector, act_vector, anx_vector = [
    [
        ["E", "A", "I"],
        ["D", "B", "T"],
        ["Q", "E", "T", "U", "O"],
        ["O", "U", "T", "E", "Q"],
        ["S", "F", "H", "K", "Z"],
        ["A", "D", "G", "J", "L"],
        [4, 8],
        [2, 4, 6, 8, 10],
        ["@", "$", "^", "*", ")", "]"],
        ["[", "(", "&", "%", "#", "!"],
        ["O", "B", "T", "Y"],
        ["R", "I", "R", "R", "L"]
    ], [
        ["E", "D", "A", "B", "I", "T"],
        ["E", "D", "A", "B", "I", "T"],
        ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["P", "O", "I", "U", "Y", "T", "R", "E", "W", "Q"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", "Z"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", "Z"],
        [2, 4, 6, 8, 10],
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "[", "]"],
        ["]", "[", ")", "(", "*", "&", "^", "%", "$", "#", "@", "!"],
        ["O", "R", "B", "I", "T", "L", "Y"],
        ["A", "R", "B", "I", "T", "R", "A", "R", "I", "L", "Y"]
    ],
    ["even", "odd", "even", "odd", "odd", "even", "even", "odd", "odd", "odd", "odd", "even"]
]
for i, x in enumerate(exp_vector):
    assert get_items_at(act_vector[i], anx_vector[i]) == x
