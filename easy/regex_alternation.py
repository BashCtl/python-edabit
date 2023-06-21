import  re
txt1 = 'red flag blue flag'
txt2 = 'yellow flag red flag blue flag green flag'
txt3 = 'pink flag red flag black flag blue flag green flag red flag'
txt4 = 'blue flag red flag red flag blue flag green flag red flag'

pattern = "red flag|blue flag"

# Test.assert_equals('|' in pattern, True, 'You must use the vertical bar alternation in your expression')
# Test.assert_equals(re.findall(pattern, txt1), ['red flag', 'blue flag'])
# Test.assert_equals(re.findall(pattern, txt2), ['red flag', 'blue flag'])
# Test.assert_equals(re.findall(pattern, txt3), ['red flag', 'blue flag', 'red flag'])
# Test.assert_equals(re.findall(pattern, txt4), ['blue flag', 'red flag', 'red flag', 'blue flag', 'red flag'])
