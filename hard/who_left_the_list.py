def missing(lst1, lst2):
    for num in lst1:
        if lst2.count(num) < lst1.count(num):
            return num


print(missing([1, 2, 3, 4, 5, 6, 7, 8], [1, 3, 4, 5, 6, 7, 8]))
print(missing([True, True, False, False, True], [False, True, False, True]))
print(missing(["Jane", "is", "pretty", "ugly"], ["Jane", "is", "pretty"]))
print(missing(["different", "types", "5", 5, [5], (5,)], ["5", "different", [5], "types", 5]))