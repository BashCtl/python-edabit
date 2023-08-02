import re

pattern = "\\d+ \\w+ \\w+\\."

txt = "123 Redding Dr. 1560 Knoxville Ave. 3030 Norwalk Dr. 5 South St."
print(re.findall(pattern, txt))