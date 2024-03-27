"""
RegEx V: Negative Lookahead


Write a regular expression that will match the states that voted no to President Trump's impeachment. You must use RegEx negative lookahead. You are not allowed to use positive lookaheads.

Example
txt = "Texas = no, California = yes, Florida = yes, Michigan = no"
pattern = "yourregularexpressionhere"

re.findall(pattern, txt) ➞ ["Texas", "Michigan"]

"""
import re
from unittest import  TestCase

txt = "Texas = no, California = yes, Florida = yes, Michigan = no"
pattern = r"(\b[A-Z]{1}[a-z]+\b)(?! = yes)"

result = re.findall(pattern, txt)
print(result)

txt = 'Texas = no, California = yes, Florida = yes, Michigan = no'

TestCase().assertEqual('(?!' in pattern, True, 'You must use negative lookahead.')
TestCase().assertEqual('(?=' in pattern, False, 'You are not allowed to use positive lookahead.')
TestCase().assertEqual(re.findall(pattern, txt), ['Texas', 'Michigan'])
