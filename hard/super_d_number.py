"""
Super-d Numbers

A number n becomes a super-d number when, for any digit d from 2 up to 9, the result of d * nᵈ contains d consecutive digits equal to d.

Given a positive integer n, implement a function that returns:

"Super-d Number" if n is a super-d number, replacing the letter d with the digit (any from 2 up to 9) that makes it super;
"Normal Number" if n is not a super-d number.
Examples
is_super_d(19) ➞ "Super-2 Number"
# when d = 2
# 2 * 19² = 722
# There are two (d) consecutives digits equal to 2 (d)

is_super_d(753) ➞ "Super-3 Number"
# when d = 3
# 3 * 753³ = 1280873331
# There are three (d) consecutives digits equal to 3 (d)

is_super_d(1168) ➞ "Super-4 Number"
# when d = 4
# 4 * 1168⁴ = 7444428488704
# There are four (d) consecutives digits equal to 4 (d)

is_super_d(24) ➞ "Normal Number"
# No cases where d * 24ᵈ (with d being any digit from 2 up to 9)...
# ...leads to a result containing d consecutive digits equal to d
Notes
Any given n will be a positive integer greater or equal to 0.


"""

import re
from unittest import TestCase


def is_super_d(n):
    for d in range(2, 10):
        result = d * n ** d
        searched = re.search(f"{d}" * d, str(result))
        if searched and searched.group() == f"{d}" * d:
            return f"Super-{d} Number"
    return "Normal Number"


TestCase().assertEqual(is_super_d(19), "Super-2 Number", "Example #1")
TestCase().assertEqual(is_super_d(753), "Super-3 Number", "Example #2")
TestCase().assertEqual(is_super_d(1168), "Super-4 Number", "Example #3")
TestCase().assertEqual(is_super_d(24), "Normal Number", "Example #4")
TestCase().assertEqual(is_super_d(20379), "Super-5 Number")
TestCase().assertEqual(is_super_d(185423), "Super-8 Number")
TestCase().assertEqual(is_super_d(1170), "Normal Number")
TestCase().assertEqual(is_super_d(118), "Normal Number")
TestCase().assertEqual(is_super_d(93568867), "Super-9 Number")
TestCase().assertEqual(is_super_d(333), "Super-2 Number")
TestCase().assertEqual(is_super_d(107), "Super-2 Number")
TestCase().assertEqual(is_super_d(1184321), "Super-7 Number")
TestCase().assertEqual(is_super_d(10098023246), "Normal Number")
TestCase().assertEqual(is_super_d(1045361), "Super-6 Number")
TestCase().assertEqual(is_super_d(0), "Normal Number", "Paradoxical Test")
