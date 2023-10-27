"""
RegEx XI-B: Whitespace Character Class
Write the regular expression that will match all whitespaces at the beginning
or the end of a string so that the re.sub() fuction in the tests (you do not need to write it)
will function like the .trim() method. Use the character class \s in your expression.

Example
txt1 = "    Hello World    "
txt2 = "    We need more space   "
pattern = "yourregularexpressionhere"

re.sub(pattern, "", txt1) ➞ "Hello World"
re.sub(pattern, "", txt2) ➞ "We need more space"

"""
import re

pattern = r"^\s+|\s+$"

txt1 = "    Hello World    "
txt2 = "    We need more space   "

print(re.sub(pattern, "", txt1))  # ➞ "Hello World"
print(re.sub(pattern, "", txt2))  # ➞ "We need more space"
