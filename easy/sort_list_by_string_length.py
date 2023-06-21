def sort_by_length(lst):
    lst.sort(key=lambda a: len(a))
    return lst


print(sort_by_length(["Google", "Apple", "Microsoft"]))
print(sort_by_length(["Leonardo", "Michelangelo", "Raphael", "Donatello"]))