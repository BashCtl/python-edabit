def move(word):
    return "".join([chr(ord(letter) + 1) for letter in word.lower()])


print(move("hello"))
