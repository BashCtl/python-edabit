import re


def vowel_links(txt):
    if re.search("(\w+[aeiou]) ([aeiou]\w+)", txt):
        return len(re.search("(\w+[aeiou]) ([aeiou]\w+)", txt).groups()) >= 2
    return False


print(vowel_links("a very large appliance"))
print(vowel_links("go to edabit"))
print(vowel_links("an open fire"))
