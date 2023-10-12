import re

pattern = r"\b\w+\b(?= \= yes)"

txt = "Texas = no, California = yes, Florida = yes, Michigan = no"

print(re.findall(pattern, txt))
