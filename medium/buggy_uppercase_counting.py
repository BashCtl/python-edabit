def count_uppercase(lst):
    return sum([len([letter for letter in word if letter.isupper()]) for word in lst])


print(count_uppercase(["SOLO", "hello", "Tea", "wHat"]))
print(count_uppercase(["little", "lower", "down"]))