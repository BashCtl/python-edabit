import re


def same_vowel_group(w):
    first = re.sub("[^aeiou]", "", w[0])
    return [w[i] for i in range(0, len(w))
            if set(re.sub("[^aeiou]", "", w[i])) == set(first)]


print(same_vowel_group(["toe", "ocelot", "maniac"]))
print(same_vowel_group(["many", "carriage", "emit", "apricot", "animal"]))