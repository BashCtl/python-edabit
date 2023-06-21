def stutter(word):
    first = word[:2]
    return "{0}... {0}... {1}?".format(first, word)


result = stutter("incredible")
print(result)
