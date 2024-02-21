"""
Recursion: Underscore-Hash Staircase


Create a function that will build a staircase using the underscore _
and hash # symbols. A positive value denotes
the staircase's upward direction and downwards for a negative value.

Examples
staircase(3) ➞ "__#\n_##\n###"
__#
_##
###

staircase(7) ➞ "______#\n_____##\n____###\n___####\n__#####\n_######\n#######"
______#
_____##
____###
___####
__#####
_######
#######

staircase(2) ➞ "_#\n##"
_#
##

staircase(-8) ➞ "########\n_#######\n__######\n___#####\n____####\n_____###\n______##\n_______#"
########
_#######
__######
___#####
____####
_____###
______##
_______#
Notes
All inputs are either positive or negative values.
The string to be returned should be adjoined with the newline character \n.
You're expected to solve this challenge using a recursive approach.

"""


def staircase(n, stair=[], h=None):
    if h == 0 or h == abs(n) + 1:
        result = "\n".join(stair)
        stair.clear()
        return result

    if not h:
        h = 1 if n > 0 else abs(n)

    row = "_" * (abs(n) - h) + "#" * h
    stair.append(row)
    h = h + 1 if n > 0 else h - 1
    return staircase(n, stair, h)


print(staircase(7))
print("=" * 20)
print(staircase(-8))
