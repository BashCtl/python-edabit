def letter_counter(lst, letter):
    return sum([l.count(letter) for l in lst])


lst = [
    ["D", "E", "Y", "H", "A", "D"],
    ["C", "B", "Z", "Y", "J", "K"],
    ["D", "B", "C", "A", "M", "N"],
    ["F", "G", "G", "R", "S", "R"],
    ["V", "X", "H", "A", "S", "S"]
]

print(letter_counter(lst, "D"))
