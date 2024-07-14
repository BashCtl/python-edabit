"""

Closing in Sum

Create a function that returns the sum of the digits formed from the first and last digits, all the way to the center of the number.

Worked Example
closing_in_sum(2520) ➞ 72

# The first and last digits are 2 and 0.
# 2 and 0 form 20.
# The second digit is 5 and the second to last digit is 2.
# 5 and 2 form 52.

# 20 + 52 = 72
Examples
closing_in_sum(121) ➞ 13
# 11 + 2

closing_in_sum(1039) ➞ 22
# 19 + 3

closing_in_sum(22225555) ➞ 100
# 25 + 25 + 25 + 25
Notes
If the number has an odd number of digits, simply add on the single-digit number in the center (see example #1).
Any number which is zero-padded counts as a single digit (see example #2).
"""

from unittest import TestCase


def closing_in_sum(n):
    s = str(n)

    def helper(s):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return int(s)
        first = int(s[0])
        last = int(s[-1])
        return int(str(first) + str(last)) + helper(s[1:-1])

    return helper(s)


TestCase().assertEqual(closing_in_sum(121), 13)
TestCase().assertEqual(closing_in_sum(1039), 22)
TestCase().assertEqual(closing_in_sum(22225555), 100)
TestCase().assertEqual(closing_in_sum(2520), 72)
TestCase().assertEqual(closing_in_sum(5332824166496569), 331)
TestCase().assertEqual(closing_in_sum(1979672314137318116), 485)
TestCase().assertEqual(closing_in_sum(1795459644013947776), 548)
TestCase().assertEqual(closing_in_sum(2801980378842185820), 426)
TestCase().assertEqual(closing_in_sum(3440584288422776554), 430)
TestCase().assertEqual(closing_in_sum(1985124000275401986), 342)
TestCase().assertEqual(closing_in_sum(1807452600132227071), 355)
TestCase().assertEqual(closing_in_sum(4319109703929506546), 389)
TestCase().assertEqual(closing_in_sum(7617065707454878893), 453)
TestCase().assertEqual(closing_in_sum(6332019057820232020), 316)
TestCase().assertEqual(closing_in_sum(901916905437689753), 452)
TestCase().assertEqual(closing_in_sum(8574963792985202586), 627)
TestCase().assertEqual(closing_in_sum(1827923410871280811), 406)
TestCase().assertEqual(closing_in_sum(1192239769354257577), 454)
TestCase().assertEqual(closing_in_sum(7565666227181120333), 479)
TestCase().assertEqual(closing_in_sum(4456731446833112446), 418)
TestCase().assertEqual(closing_in_sum(6649112211153605642), 353)
TestCase().assertEqual(closing_in_sum(6043414146315434510), 302)
TestCase().assertEqual(closing_in_sum(2154880710356439481), 403)
TestCase().assertEqual(closing_in_sum(9879403672023435605), 560)
