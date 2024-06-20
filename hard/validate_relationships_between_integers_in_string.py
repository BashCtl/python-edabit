"""
Validate the Relationships Between Integers in a String


You will be given a string consisting of a list of integers and their relationships to their neighboring integers. For instance:

"-15<-10<=0=0<5"
Test to see that all the relationships between the integers in the string are true. If they are, return True. If they are not, return False.

Examples
validate_relationships("5>-1<0=0<-5>5=5") ➞ False
# This is False because 0 is not less than -5.

validate_relationships("-15<-10<=0=0<5") ➞ True

validate_relationships("0=807<1000<=1000>9990<-3605<=20") ➞ False
# This is False because 0 is not equal to 807.
Notes
This is a modifcation of Helen Yu's "Correct Signs" challenge.
As the examples above show, there could be negative numbers in the string.
The numbers will only be separated by: =, <, >, >=, <=
Tests will not contain any spaces.

"""

import re

from unittest import TestCase


def validate_relationships(txt):
    exp = re.sub(r"[-]?(?<=\d)=((?=\d)|(?=-\d))", "==", txt)
    return eval(exp)


TestCase().assertEqual(validate_relationships("5>-1<0=0<-5>5=5"), False)
TestCase().assertEqual(validate_relationships("-15<-10<=0=0<5"), True)
TestCase().assertEqual(validate_relationships("0=807<1000<=1000>9990<-3605<=20"), False)
TestCase().assertEqual(validate_relationships("3<=3<11>-109"), True)
TestCase().assertEqual(validate_relationships("44>-33>=1>-13"), False)
TestCase().assertEqual(validate_relationships("10>2=22>9>3"), False)
TestCase().assertEqual(validate_relationships("44>0<13>=-2<-1=-1"), True)
TestCase().assertEqual(validate_relationships("3>=-1"), True)
TestCase().assertEqual(validate_relationships("9<=9<-1"), False)
TestCase().assertEqual(validate_relationships("0<9<=9>-1"), True)
TestCase().assertEqual(validate_relationships("44>=0<13>-2<-1=1"), False)
TestCase().assertEqual(validate_relationships("-39<=5=5<=9>-1"), True)
TestCase().assertEqual(validate_relationships("55>7>=7>=1"), True)
TestCase().assertEqual(validate_relationships("3<19>-19>5>=-19"), False)
