def hangman(phrase, lst):
    return "".join([symbol if symbol.lower() in lst or not symbol.isalpha() else "-"
                    for symbol in phrase])


print(hangman("helicopter", ["o", "e", "s"]))
print(hangman("tree", ["r", "t", "e"]))
print(hangman("Python rules", ["a", "n", "p", "r", "z"]))
print(hangman("He\"s a very naughty boy!", ["e", "a", "y"]))
