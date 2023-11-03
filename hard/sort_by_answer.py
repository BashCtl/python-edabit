"""
Sort by Answer

Given a list of math expressions, create a function which sorts the list by their answer.
It should be sorted in ascending order.

Examples
sort_by_answer(["1 + 1", "1 + 7", "1 + 5", "1 + 4"]) ➞ ["1 + 1", "1 + 4", "1 + 5", "1 + 7"]

sort_by_answer(["4 - 4", "2 - 2", "5 - 5", "10 - 10"]) ➞ ["4 - 4", "2 - 2", "5 - 5", "10 - 10"]

sort_by_answer(["2 + 2", "2 - 2", "2 * 1"]) ➞ ["2 - 2", "2 * 1", "2 + 2"]

Notes
If multiple expressions have the same answer, put them in the order of which they appear (see example #2).
You won't need to worry about divisions by zero.
The symbol used for multiplication is x instead of *.
"""


def sort_by_answer(lst):
    func = lambda item: eval(item.replace(" ", "").replace("x", "*"))
    return sorted(lst, key=func)


print(sort_by_answer(["1 + 1", "1 + 7", "1 + 5", "1 + 4"]))
print(sort_by_answer(["2 + 2", "2 - 2", "2 x 2", "2 / 2"]))
