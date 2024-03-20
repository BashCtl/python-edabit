import re
from unittest import TestCase

"""
Recursion: License Plate

Traveling through Europe one needs to pay attention to how 
the license plate in the given country is displayed. 
When crossing the border you need to park on the shoulder,
 unscrew the plate, re-group the characters according 
 to the local regulations, attach it back and proceed with the journey.

Create a solution that can format the dmv number into a plate 
number with correct grouping. The function input consists of string s 
and group length n. The output has to be upper case characters and digits. 
The new groups are made from right to left and connected by -. 
The original order of the dmv number is preserved.

Examples
license_plate("5F3Z-2e-9-w", 4) ➞ "5F3Z-2E9W"

license_plate("2-5g-3-J", 2) ➞ "2-5G-3J"

license_plate("2-4A0r7-4k", 3) ➞ "24-A0R-74K"

license_plate("nlj-206-fv", 3) ➞ "NL-J20-6FV"
Notes
You are expected to solve this challenge via a recursive approach.

"""
def license_plate(code, group):
    code = re.sub("-", '', code).upper()
    if len(code) <= group:
        return code

    return license_plate(code[0:len(code) - group], group) + "-" + code[len(code) - group:]


str_vector = [
    ["5F3Z-2e-9-w", 4], ["2-5g-3-J", 2], ["2-4A0r7-4k", 3], ["GB-bd519-KFC", 2], ["BF-11gf9i-7819iT", 3],
    ["Fin-Mmg-418", 3], ["sPx-o755", 3], ["de57-uk", 2], ["d-kapa-7778", 4], ["nlj-206-fv", 3]
]
res_vector = [
    "5F3Z-2E9W", "2-5G-3J", "24-A0R-74K", "GB-BD-51-9K-FC", "BF-11G-F9I-781-9IT", "FIN-MMG-418", "S-PXO-755",
    "DE-57-UK", "D-KAPA-7778", "NL-J20-6FV"
]
for i, c in enumerate(str_vector):
    TestCase().assertEqual(license_plate(*c), res_vector[i])
