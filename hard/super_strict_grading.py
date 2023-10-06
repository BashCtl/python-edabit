def who_passed(students):
    func = lambda item: all(eval(v) == 1 for v in item[1])
    return sorted(dict(filter(func, students.items())).keys())


print(who_passed({
    "John": ["5/5", "50/50", "10/10", "10/10"],
    "Sarah": ["4/8", "50/57", "7/10", "10/18"],
    "Adam": ["8/10", "22/25", "3/5", "5/5"],
    "Barry": ["3/3", "20/20"]
}))

print(who_passed({
    "Zara": ["10/10"],
    "Kris": ["30/30"],
    "Charlie": ["100/100"],
    "Alex": ["1/1"]
}))

print(who_passed({
    "Zach": ["10/10", "2/4"],
    "Fred": ["7/9", "2/3"]
}))
