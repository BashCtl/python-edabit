def encrypt(word):
    word = word[::-1]
    vowels = {"a": "0", "e": "1", "i": "2", "o": "2", "u": "3"}
    return "".join([vowels[letter] if letter in vowels else letter for letter in word])+"aca"


print(encrypt("banana"))
print(encrypt("karaca"))
print(encrypt("burak"))