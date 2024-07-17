"""
A Circle and Two Squares

Imagine a circle and two squares: a smaller and a bigger one. For the smaller one, the circle is a circumcircle and for the bigger one, an incircle.

Scale

Create a function, that takes an integer (radius of the circle) and returns the difference of the areas of the two squares.

Examples
square_areas_difference(5) ➞ 50

square_areas_difference(6) ➞ 72

square_areas_difference(7) ➞ 98
Notes
Uses only positive integer parameters.
"""

from unittest import TestCase
import math


def square_areas_difference(radius):
    side_larger_square = 2 * radius
    area_larger_square = side_larger_square ** 2

    side_smaller_square = math.sqrt(radius ** 2 + radius ** 2)
    area_smaller_square = round(side_smaller_square ** 2)

    difference = area_larger_square - area_smaller_square

    return difference


TestCase().assertEqual(square_areas_difference(5), 50)
TestCase().assertEqual(square_areas_difference(6), 72)
TestCase().assertEqual(square_areas_difference(7), 98)
TestCase().assertEqual(square_areas_difference(17), 578)
