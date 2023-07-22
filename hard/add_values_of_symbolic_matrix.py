def check_score(s):
    symbols = {"#": 5, "O": 3, "X": 1, "!": -1, "!!": -3, "!!!": -5}
    result = sum([sum([symbols[k] for k in row]) for row in s])
    return result if result > 0 else 0


data = [
    ["!!!", "O", "!"],
    ["X", "#", "!!!"],
    ["!!", "X", "O"]
]

print(check_score(data))
