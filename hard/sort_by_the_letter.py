import re


def sort_by_letter(lst):
    return sorted(lst, key=lambda item: re.sub(r"\d", "", item))


print(sort_by_letter(["932c", "832u32", "2344b"]))
print(sort_by_letter(["572z", "5y5", "304q2"]))
print(sort_by_letter([]))