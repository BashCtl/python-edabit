"""
Sort by Length

Create a function that takes a string and returns a string
ordered by the length of the words. From shortest to longest word.
If there are words with the same amount of letters, order them alphabetically.

Examples
sort_by_length("Hello my friend") ➞ "my Hello friend"

sort_by_length("Have a wonderful day") ➞ "a day Have wonderful"

sort_by_length("My son loves pineapples") ➞ "My son loves pineapples"

Notes
Punctuation (periods, commas, etc) belongs to the word in front of it.


"""


def sort_by_length(txt):
    words = txt.split(" ")
    return ' '.join(sorted(words, key=lambda a: (len(a), a.lower())))


print(sort_by_length("Hello my friend"))
print(sort_by_length("To be or not to be, that is the question."))
