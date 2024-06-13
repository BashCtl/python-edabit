"""
Get Free Wi-Fi Anywhere You Go


A new 'hacky' phone is launched, which has the feature of connecting to any Wi-Fi network from any distance away, as long as there aren't any obstructions between the hotspot and the phone. Given a string, return how many Wi-Fi hotspots I'm able to connect to.

The phone is represented as a P.
A hotspot is represented as an *.
An obstruction is represented as a #. You cannot access a hotspot if they are behind one of these obstructions.
Examples
nonstop_hotspot("*   P  *   *") ➞ 3

nonstop_hotspot("*  * #  * P # * #") ➞ 1

nonstop_hotspot("***#P#***") ➞ 0
Notes
There will be only one phone.
No other characters, other than spaces, will appear in the tests

"""

from  unittest import  TestCase

import re


def nonstop_hotspot(s):
    segments = re.split(r'#', s)

    for segment in segments:
        if 'P' in segment:
            phone_segment = segment
            break
    hotspots = phone_segment.count('*')

    return hotspots




TestCase().assertEqual(nonstop_hotspot('*   P  *   *'), 3)
TestCase().assertEqual(nonstop_hotspot('*  * #  * P # * #'), 1)
TestCase().assertEqual(nonstop_hotspot('***#P#***'), 0)
TestCase().assertEqual(nonstop_hotspot('#P#'), 0)
TestCase().assertEqual(nonstop_hotspot('P'), 0)
TestCase().assertEqual(nonstop_hotspot('P       #'), 0)
TestCase().assertEqual(nonstop_hotspot('P     *  # *'), 1)
TestCase().assertEqual(nonstop_hotspot('*   # * P'), 1)
TestCase().assertEqual(nonstop_hotspot('# *****  **  P     ** #    '), 9)