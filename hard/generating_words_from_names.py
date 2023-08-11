def anagram(name, words):
    return sorted(name.replace(" ", "").lower()) == sorted([i for word in words for i in word])


print(anagram("Natalie Portman", ["ornamental", "pita"]))
print(anagram("Chris Pratt", ["chirps", "rat"]))