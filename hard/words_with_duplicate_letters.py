def no_duplicate_letters(phrase):
    words = phrase.lower().split(" ")
    return all([len(set(word)) == len(word) for word in words])


print(no_duplicate_letters("Fortune favours the bold."))
print(no_duplicate_letters("You can lead a horse to water, but you can't make him drink."))
print(no_duplicate_letters("Look before you leap."))
print(no_duplicate_letters("Always be closing."))