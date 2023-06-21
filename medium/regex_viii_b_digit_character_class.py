import re

pattern = r"\D+"

txt = "242Edabit2345can3443be3254324addictive!"
print(" ".join(re.findall(pattern, txt)))