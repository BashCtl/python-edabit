"""
Spaces Apart

Create a function that takes an lst and returns the sum of the numbers between two "1"s.

Examples
space_apart([1, 0, 1, "1", 4, 3, 2, 3, 2, "1"]) ➞ 14

space_apart(["1", 9, 20, 38, "1"]) ➞ 67

space_apart([3, 2, 9, "1", 0, 0, -1, "1"]) ➞ "invalid"

Notes
Return "invalid" if:
A negative number exists inside lst.
The number of "1"s does not equal 2.
Ignore any other string inside lst.
Note that "1" is not 1.


"""


def space_apart(lst):
    if lst.count("1") == 2:
        first_index = lst.index("1")
        last_index = len(lst) - 1 - lst[::-1].index("1")
        if 0 <= first_index != last_index >= 0:
            sub_list = [x for x in lst[first_index + 1: last_index] if type(x) == int]
            if all([n >= 0 for n in sub_list]):
                return sum(sub_list)
    return "invalid"


print(space_apart([1, 0, 1, "1", 4, 3, 2, 3, 2, "1"]))
print(space_apart(["1", 9, 20, 38, "1"]))
print(space_apart([3, 2, 9, "1", 0, 0, -1, "1"]))
print(space_apart(["1"]))
print(space_apart([4, 3, "1", "2", 4, "1", "2", "9"]))
