from unittest import TestCase

"""
Maxie and Minnie

Maxie is the largest number that can be obtained by swapping two digits, 
Minnie is the smallest. Write a function that takes a number and returns 
Maxie and Minnie. Leading zeros are not permitted.

Examples
maxmin(12340) ➞ (42310, 10342)

maxmin(98761) ➞ (98761, 18769)

maxmin(9000) ➞ (9000, 9000)
# Sometimes no swap needed.

maxmin(11321) ➞ (31121, 11123)

"""


def maxmin(num):
    str_num = str(num)
    max_num = num
    min_num = num
    length = len(str_num)
    for i in range(length):
        for j in range(i + 1, length):
            numbers = list(str_num)
            numbers[i], numbers[j] = numbers[j], numbers[i]
            if numbers[0] != '0':
                max_num = max(max_num, int(''.join(numbers)))
                min_num = min(min_num, int(''.join(numbers)))

    return max_num, min_num


TestCase().assertEqual(maxmin(9876543210), (9876543210, 1876543290))
TestCase().assertEqual(maxmin(1234567890), (9234567810, 1034567892))
TestCase().assertEqual(maxmin(190015878798001), (990015878718001, 100015878798091))
TestCase().assertEqual(maxmin(411347917692022), (911347917642022, 111347947692022))
TestCase().assertEqual(maxmin(91620336331950), (99620336331150, 11620336339950))
TestCase().assertEqual(maxmin(428256072523076), (824256072523076, 228256072543076))
TestCase().assertEqual(maxmin(999607251369567), (999907251366567, 199607259369567))
TestCase().assertEqual(maxmin(10936404093733), (90936404013733, 10036404993733))
TestCase().assertEqual(maxmin(116962727585478), (916162727585478, 112962767585478))
TestCase().assertEqual(maxmin(645440811595719), (945440811595716, 145440811595769))
TestCase().assertEqual(maxmin(304732653285373), (804732653235373, 204732653385373))
TestCase().assertEqual(maxmin(734694929081563), (934694927081563, 134694929087563))
TestCase().assertEqual(maxmin(597202395684464), (997202355684464, 297205395684464))
TestCase().assertEqual(maxmin(111090753368874), (911010753368874, 101091753368874))
TestCase().assertEqual(maxmin(357758017083851), (857758017083351, 157758017083853))
TestCase().assertEqual(maxmin(744888865698909), (944888865698907, 447888865698909))
TestCase().assertEqual(maxmin(589067130451808), (985067130451808, 189067130455808))
TestCase().assertEqual(maxmin(236077600527389), (936077600527382, 206077603527389))
TestCase().assertEqual(maxmin(405272406161141), (705242406161141, 105272406161144))
TestCase().assertEqual(maxmin(21460234556134), (61460234552134, 11460234556234))
TestCase().assertEqual(maxmin(347435942637955), (947435942637355, 247435943637955))
TestCase().assertEqual(maxmin(942631615759140), (992631615754140, 142631615759940))
