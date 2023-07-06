def char_appears(sentence, char):
    words = sentence.lower().split(" ")
    return [word.count(char.lower()) for word in words]


print(char_appears("She sells sea shells by the seashore.", "s"))
