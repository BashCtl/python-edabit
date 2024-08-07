"""
Up the Hill, Down the Hill

If a person traveled up a hill for 18mins at 20mph and then traveled back down the same path at 60mph then their average speed traveled was 30mph.

Write a function that returns the average speed traveled given an uphill time, uphill rate and a downhill rate. Uphill time is given in minutes. Return the rate as an integer (mph). No rounding is necessary.

Examples
ave_spd(18, 20, 60) ➞ 30

ave_spd(30, 10, 30) ➞ 15

ave_spd(30, 8, 24) ➞ 12
Notes
The solution is not dividing the sum of the speeds by 2.
Check the Resources tab if your stuck.

"""

from unittest import TestCase


def ave_spd(uphill_time, uphill_rate, downhill_rate):
    uphill_time_hours = uphill_time / 60.0

    distance_uphill = uphill_rate * uphill_time_hours

    distance_downhill = distance_uphill
    downhill_time_hours = distance_downhill / downhill_rate

    total_distance = distance_uphill + distance_downhill
    total_time_hours = uphill_time_hours + downhill_time_hours

    average_speed = total_distance / total_time_hours

    return int(average_speed)


TestCase().assertEqual(ave_spd(18, 10, 30), 15)
TestCase().assertEqual(ave_spd(18, 20, 60), 30)
TestCase().assertEqual(ave_spd(30, 10, 30), 15)
TestCase().assertEqual(ave_spd(30, 8, 24), 12)
