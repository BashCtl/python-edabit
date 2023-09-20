import re

pattern = r"\b(?:a|an|the) \b\w+\b"

txt = "There is an apple and a pen on the desk"

print(re.findall(pattern, txt))
txt2 = 'They say: an apple a day keeps the doctor away'
print(re.findall(pattern, txt2))
txt3 = 'In Antarctica the temperature is quite low'
print(re.findall(pattern,txt3))