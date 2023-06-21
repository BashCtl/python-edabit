def sum_of_vowels(sentence):
    vowels = {"a": 4, "e": 3, "i": 1, "o": 0, "u": 0}
    return sum([vowels[k] if k in vowels else 0 for k in sentence.lower()])


print(sum_of_vowels("Do I get the correct output?"))
