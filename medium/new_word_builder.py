def word_builder(ltr, pos):
    return "".join([ltr[i] for i in pos])


print(word_builder(["g", "e", "o"], [1, 0, 2]))