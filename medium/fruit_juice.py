"""
Fruit Juices
A fruit juice company tags their fruit juices by concatenating the first three letters of the words in a flavor's name, with its capacity.

Create a function that creates product IDs for different fruit juices.

Examples
get_drink_ID("apple", "500ml") ➞ "APP500"

get_drink_ID("pineapple", "45ml") ➞ "PIN45"

get_drink_ID("passion fruit", "750ml") ➞ "PASFRU750"
Notes
Capacity will be given as a string, and will always be given in ml.
Return the letters in UPPERCASE.

"""


from unittest import TestCase


def get_drink_ID(flavor, ml):
    fl = "".join([f[:3] for f in flavor.split(" ")]).upper()
    return fl + ml[:-2]


TestCase().assertEqual(get_drink_ID("apple", "500ml"), "APP500")
TestCase().assertEqual(get_drink_ID("pineapple", "45ml"), "PIN45")
TestCase().assertEqual(get_drink_ID("orange", "750ml"), "ORA750")
TestCase().assertEqual(get_drink_ID("passion fruit", "1ml"), "PASFRU1")
TestCase().assertEqual(get_drink_ID("mango", "1000ml"), "MAN1000")
TestCase().assertEqual(get_drink_ID("very berry", "253ml"), "VERBER253")
TestCase().assertEqual(get_drink_ID("raspberry and lime", "350ml"), "RASANDLIM350")
