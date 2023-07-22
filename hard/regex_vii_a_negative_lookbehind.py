import re

pattern = r"(?<!good) cookie"


lst = ["bad cookie", "good cookie", "bad cookie", "good cookie", "good cookie"]

print(len(re.findall(pattern, ", ".join(lst))))