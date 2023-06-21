def count_vowels(txt):
    result = 0
    for i in "aeiou":
        result += txt.count(i)
    return result


print(count_vowels("Celebration"))
print(count_vowels("Palm"))
