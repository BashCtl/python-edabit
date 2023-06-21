import re

pattern = r"[^\w\d ]"

txt = " alice15@gmail.com "

print(re.findall(pattern, txt))