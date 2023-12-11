from unittest import TestCase

"""
Pile of Cubes

Mubashir needs your help to construct a building which will be
 a pile of n cubes. The cube at the bottom will have 
 a volume of n^3, the cube above will have volume 
 of (n-1)^3 and so on until the top which will have a volume of 1^3.

Given the total volume m of the building, can you find the number of cubes n required for the building?

In other words, you have to return an integer n such that:

n^3 + (n-1)^3 + ... + 1^3 == m
Return None if there is no such number.

Examples
pile_of_cubes(1071225) ➞ 45

pile_of_cubes(4183059834009) ➞ 2022

pile_of_cubes(16) ➞ None


"""


def pile_of_cubes(m):
    total = 0
    n = 0

    while total < m:
        n += 1
        total += n ** 3

    return n if total == m else None


TestCase().assertEqual(pile_of_cubes(4183059834009), 2022)
TestCase().assertEqual(pile_of_cubes(24723578342962), None)
TestCase().assertEqual(pile_of_cubes(135440716410000), 4824)
TestCase().assertEqual(pile_of_cubes(40539911473216), 3568)
TestCase().assertEqual(pile_of_cubes(26825883955641), 3218)
TestCase().assertEqual(pile_of_cubes(41364076483082), None)
TestCase().assertEqual(pile_of_cubes(9541025211025), 2485)
TestCase().assertEqual(pile_of_cubes(112668204662785), None)
TestCase().assertEqual(pile_of_cubes(79172108332642), None)
TestCase().assertEqual(pile_of_cubes(1788719004901), None)
TestCase().assertEqual(pile_of_cubes(131443152397956), 4788)
TestCase().assertEqual(pile_of_cubes(1801879360282), None)
TestCase().assertEqual(pile_of_cubes(18262169777476), 2923)
TestCase().assertEqual(pile_of_cubes(11988186060816), 2631)
TestCase().assertEqual(pile_of_cubes(826691919076), 1348)
TestCase().assertEqual(pile_of_cubes(36099801072722), None)
TestCase().assertEqual(pile_of_cubes(171814395026), None)
TestCase().assertEqual(pile_of_cubes(637148782657), None)
TestCase().assertEqual(pile_of_cubes(6759306226), None)
TestCase().assertEqual(pile_of_cubes(33506766981009), 3402)
TestCase().assertEqual(pile_of_cubes(108806345136785), None)
TestCase().assertEqual(pile_of_cubes(14601798712901), None)
TestCase().assertEqual(pile_of_cubes(56454575667876), 3876)
TestCase().assertEqual(pile_of_cubes(603544088161), 1246)
TestCase().assertEqual(pile_of_cubes(21494785321), 541)
TestCase().assertEqual(pile_of_cubes(4), None)
TestCase().assertEqual(pile_of_cubes(16), None)
TestCase().assertEqual(pile_of_cubes(1025292944081385001), 45001)
TestCase().assertEqual(pile_of_cubes(10252519345963644753025), 450010)
TestCase().assertEqual(pile_of_cubes(10252519345963644753026), None)
TestCase().assertEqual(pile_of_cubes(102525193459636447530260), None)
