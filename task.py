import re

with open("main.txt", "r") as file:
    f = file.read()
    result = re.findall("[^aeiou]", f)
    print(len(result))

