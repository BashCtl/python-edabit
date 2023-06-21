def is_anagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return sorted(s1) == sorted(s2)


print(is_anagram("cristian", "Cristina"))
print(is_anagram("Dave Barry", "Ray Adverb"))
print(is_anagram("Nope", "Note"))