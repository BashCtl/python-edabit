from unittest import TestCase

"""
Let's Meet!

From point A, an object is moving towards point B at constant velocity va (in km/hr). 
From point B, another object is moving towards point A at constant velocity vb (in km/hr). 
Knowing this and the distance between point A and B (in km), 
write a function that returns how much time passes until both objects meet.

Format the output like this:

"2h 23min 34s"
Examples
lets_meet(100, 10, 30) ➞ "2h 30min 0s"

lets_meet(280, 70, 80) ➞ "1h 52min 0s"

lets_meet(90, 75, 65) ➞ "0h 38min 34s"
Notes
Seconds should be rounded down to the nearest whole number.
"""


def lets_meet(distance, va, vb):
    hours = distance / (va + vb)
    minutes = hours % 1 * 60
    seconds = minutes % 1 * 60
    return "{}h {}min {}s".format(int(hours), int(minutes), int(seconds))


TestCase().assertEqual(lets_meet(100, 10, 30), "2h 30min 0s")
TestCase().assertEqual(lets_meet(33, 15, 20), "0h 56min 34s")
TestCase().assertEqual(lets_meet(250, 60, 80), "1h 47min 8s")
TestCase().assertEqual(lets_meet(125, 55, 40), "1h 18min 56s")
TestCase().assertEqual(lets_meet(0.6, 10, 15), "0h 1min 26s")
TestCase().assertEqual(lets_meet(0.8, 23, 18), "0h 1min 10s")
TestCase().assertEqual(lets_meet(0.72, 8, 12), "0h 2min 9s")
TestCase().assertEqual(lets_meet(33, 15, 20), "0h 56min 34s")
TestCase().assertEqual(lets_meet(360, 80, 64), "2h 30min 0s")
TestCase().assertEqual(lets_meet(10, 45, 42), "0h 6min 53s")
TestCase().assertEqual(lets_meet(90, 75, 65), "0h 38min 34s")
TestCase().assertEqual(lets_meet(280, 70, 80), "1h 52min 0s")
