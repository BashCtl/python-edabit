"""
Snail Crawl out of the Bucket
A snail fell into a bucket and wanted to crawl out. Assuming we already know the snail can climb 5cm per minute, the snail can crawl for 30 minutes continuously and then needs to rest for 10 minutes. When it is resting it will slide down 30cm.

How many minutes will it take for the snail to crawl out from different depths? Create a function that takes the bucket depth (the unit is cm) as an argument and returns the time in minutes.

if depth = 270
the snail crawling process
process: (150 - 30) +  150
minutes: (30+10) + 150 / 5
it will take 70 minutes
the last 150cm, the snail doesn't need a rest
Examples
cal(31) ➞ 7

cal(150) ➞ 30

cal(200) ➞ 56
Notes
The depth is a positive integer.
If the time is less than one minute it still counts as one minute.


"""
from unittest import TestCase


def cal(depth):
    time = 0
    current_depth = 0
    while current_depth < depth:
        if current_depth + 150 < depth:
            current_depth += 150
            time += 30
        else:
            remaining_depth = depth - current_depth
            time += remaining_depth // 5
            if remaining_depth % 5 != 0:
                time += 1
            break

        current_depth -= 30
        time += 10

    return time


TestCase().assertEqual(cal(31), 7, "Examples 1")
TestCase().assertEqual(cal(150), 30, "Examples 2")
TestCase().assertEqual(cal(200), 56, "Examples 3")
TestCase().assertEqual(cal(15), 3)
TestCase().assertEqual(cal(151), 47)
TestCase().assertEqual(cal(160), 48)
TestCase().assertEqual(cal(300), 92)
