import re


def get_prices(lst):
    return [float(re.sub(r"[^\d\.]","", price)) for price in lst]


print(get_prices(["salad ($4.99)"]))
print(get_prices([
  "ice cream ($5.99)",
  "banana ($0.20)",
  "sandwich ($8.50)",
  "soup ($1.99)"
]))