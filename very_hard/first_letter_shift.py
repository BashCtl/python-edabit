def shift_sentence(txt):
    words = txt.split()
    first_letters = [word[0] for word in words]
    first_letters.insert(0, first_letters.pop())
    words = [first_letters[i] + words[i][1:] for i in range(len(words))]
    return " ".join(words)


print(shift_sentence("create a function"))
print(shift_sentence("it should shift the sentence"))
