"""
Combine Arrays

Create a function that takes three lists and returns one list where
all passed arrays are combined into nested lists.

These lists should be combined based on indexes: the first nested list should contain only
the items on index 0, the second list on index 1, and so on.

If any list contains fewer items than necessary, supplement the missing item with "*".

Examples
combine_lists([False, "False"], ["True", True, "bool"], ["None", "undefined"]) ➞ [[False, "True", "None"], ["False", True, "undefined"], ["*", "bool", "*"]]

combine_lists([1, 2, 3], [4, 5, 6], [7, 8, 9]) ➞ [[1, 4, 7], [2, 5,  8], [3, 6, 9]]

combine_lists(["Jack", "Joe", "Jill"], ["Stuart", "Sammy", "Silvia"], ["Rick", "Raymond", "Riri"]) ➞ [["Jack", "Stuart", "Rick"], ["Joe", "Sammy",  "Raymond"], ["Jill", "Silvia", "Riri"]]
"""


def combine_lists(lst1, lst2, lst3):
    max_length = max(len(lst1), len(lst2), len(lst3))
    lst1 += ['*'] * (max_length - len(lst1))
    lst2 += ['*'] * (max_length - len(lst2))
    lst3 += ['*'] * (max_length - len(lst3))

    return [[x, y, z] for x, y, z in zip(lst1, lst2, lst3)]


print(combine_lists([False, "False"], ["True", True, "bool"], ["None", "undefined"]))
