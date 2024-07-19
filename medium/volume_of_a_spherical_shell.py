"""
Volume of a Spherical Shell
The volume of a spherical shell is the difference between the enclosed volume of the outer sphere and the enclosed volume of the inner sphere:

Volume of Inner Sphere Formula

Create a function that takes r1 and r2 as arguments and returns the volume of a spherical shell rounded to the nearest thousandth.

Spherical Shell Image

Examples
vol_shell(3, 3) ➞ 0

vol_shell(7, 2) ➞ 1403.245

vol_shell(3, 800) ➞ 2144660471.753
Notes
The inputs are always positive numbers. r1 could be the inner radius or the outer radius, don't return a negative number.
"""

from unittest import TestCase
import math


def vol_shell(r1, r2):
    outer_radius = max(r1, r2)
    inner_radius = min(r1, r2)

    volume_outer = (4 / 3) * math.pi * outer_radius ** 3
    volume_inner = (4 / 3) * math.pi * inner_radius ** 3

    volume_shell = volume_outer - volume_inner

    return round(volume_shell, 3)


TestCase().assertEqual(vol_shell(17, 36), 174852.67)
TestCase().assertEqual(vol_shell(3, 4), 154.985)
TestCase().assertEqual(vol_shell(1, 90), 3053623.87)
TestCase().assertEqual(vol_shell(12.5, 19), 20549.681)
TestCase().assertEqual(vol_shell(3, 800), 2144660471.753)
TestCase().assertEqual(vol_shell(16.128, 16.256), 421.719)
TestCase().assertEqual(vol_shell(3, 3), 0)
TestCase().assertEqual(vol_shell(4, 3), 154.985)
TestCase().assertEqual(vol_shell(36, 17), 174852.67)
TestCase().assertEqual(vol_shell(18, 96), 3681544.466)
TestCase().assertEqual(vol_shell(1, 7), 1432.566)
TestCase().assertEqual(vol_shell(7, 2), 1403.245)
TestCase().assertEqual(vol_shell(100, 50), 3665191.429)
TestCase().assertEqual(vol_shell(40, 36), 72650.377)
