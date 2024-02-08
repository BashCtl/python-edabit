"""
Building a Staircase

Create a function that builds a staircase given the height and the type of building block.

Examples
build_staircase(3, "#") ➞ [
  ["#", "_", "_"],
  ["#", "#", "_"],
  ["#", "#", "#"]
]

build_staircase(4, "#") ➞ [
  ["#", "_", "_", "_"],
  ["#", "#", "_", "_"],
  ["#", "#", "#", "_"],
  ["#", "#", "#", "#"]
]

build_staircase(3, "A") ➞ [
  ["A", "_", "_"],
  ["A", "A", "_"],
  ["A", "A", "A"]
]

# height = 3 and building block = "A"

build_staircase(4, "$") ➞ [
  ["$", "_", "_", "_"],
  ["$", "$", "_", "_"],
  ["$", "$", "$", "_"],
  ["$", "$", "$", "$"]
]

# height = 4 and building block = "$"
Notes
If the height is 0, return an empty list [].

"""


def build_staircase(height, block):
    return [[block if i <= r else "_" for i in range(height)] for r in range(height)]


print(build_staircase(3, "#"))
