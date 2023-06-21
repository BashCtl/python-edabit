def name_shuffle(txt):
    names = txt.split(" ")
    names =list(reversed(names))
    return " ".join(names)


print(name_shuffle("Donald Trump"))
print(name_shuffle("Rosie O'Donnell"))
print(name_shuffle("Seymour Butts"))
