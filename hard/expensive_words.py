def get_sentence_value(txt):
    total = 0
    for word in txt.split(" "):
        word_sum = sum([ord(l) - ord('a') + 1 for l in word.lower() if l.isalpha()])
        if word.isupper():
            total += word_sum * 2
        else:
            total += word_sum
    return total


print(get_sentence_value("abc ABC Abc"))
print(get_sentence_value("HELLO world"))
print(get_sentence_value("Edabit is LEGENDARY"))
print(get_sentence_value("Her seaside sea-shelling business is really booming!"))
