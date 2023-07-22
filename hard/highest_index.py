def alphabet_index(alphabet, string):
    string = string.lower()
    alpha_dict = {x: i + 1 for i, x in enumerate(alphabet)}
    highest = 0
    key = ""
    for l in string:
        if l in alpha_dict and alpha_dict[l] > highest:
            highest = alpha_dict[l]
            key = l
    return "{}{}".format(alpha_dict[key],key)


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

print(alphabet_index(alphabet, "Flavio"))
