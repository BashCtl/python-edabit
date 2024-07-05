"""

String Expansion

Create a function that takes a string txt and expands it as per the following rules:

The numeric values represent the occurrence of each letter preceding that numeric value.
string_expansion("3M2u5b2a1s1h2i1r") ➞ "MMMuubbbbbaashiir"
The first occurrence of a numeric value should be the number of times each character behind it is repeated, until the next numeric value appears.
string_expansion("3Mat")➞ "MMMaaattt"      # correct

string_expansion("3Mat") ➞ "MMMat"          # wrong
string_expansion("3Mat") ➞ "MatMatMat"      # wrong
If there are consecutive numeric characters, ignore them all except last one.
string_expansion("3M123u42b12a") ➞ "MMMuuubbaa"
If there are two consecutive alphabetic characters then the string will remain unchanged.
string_expansion("airforce") ➞ "airforce"
Empty strings should return an empty string.
string_expansion("") ➞ ""

"""

from unittest import TestCase


def string_expansion(txt):
    if not txt:
        return ""

    result = []
    multiplier = 1

    for i, char in enumerate(txt):
        if char.isdigit():
            multiplier = int(char)
        else:
            result.append(char * multiplier)

    return "".join(result)



TestCase().assertEqual(string_expansion("3M2u5b2a1s1h2i1r"),"MMMuubbbbbaashiir")
TestCase().assertEqual(string_expansion("3Mat"),"MMMaaattt")
TestCase().assertEqual(string_expansion("3M123u42b12a"),"MMMuuubbaa")
TestCase().assertEqual(string_expansion("3n6s7f3n"),"nnnssssssfffffffnnn")
TestCase().assertEqual(string_expansion("0d4n8d2b"),"nnnnddddddddbb")
TestCase().assertEqual(string_expansion("0c3b1n7m"),"bbbnmmmmmmm")
TestCase().assertEqual(string_expansion("7m3j4ik2a"),"mmmmmmmjjjiiiikkkkaa")
TestCase().assertEqual(string_expansion("3A5m3B3Y"),"AAAmmmmmBBBYYY")
TestCase().assertEqual(string_expansion("5M0L8P1"),"MMMMMPPPPPPPP")
TestCase().assertEqual(string_expansion("2B"),"BB")
TestCase().assertEqual(string_expansion("7M1n3K"),"MMMMMMMnKKK")
TestCase().assertEqual(string_expansion("A4g1b4d"),"Aggggbdddd")
TestCase().assertEqual(string_expansion("111111"),"")
TestCase().assertEqual(string_expansion("4d324n2"),"ddddnnnn")
TestCase().assertEqual(string_expansion("5919nf3u"),"nnnnnnnnnfffffffffuuu")
TestCase().assertEqual(string_expansion("2n1k523n4i"),"nnknnniiii")
TestCase().assertEqual(string_expansion("6o23M32d"),"ooooooMMMdd")
TestCase().assertEqual(string_expansion("1B44n3r"),"Bnnnnrrr")
TestCase().assertEqual(string_expansion("M21d1r32"),"Mdr")
TestCase().assertEqual(string_expansion("23M31r2r2"),"MMMrrr")
TestCase().assertEqual(string_expansion("8494mM25K2A"),"mmmmMMMMKKKKKAA")
TestCase().assertEqual(string_expansion("4A46D6B3C"),"AAAADDDDDDBBBBBBCCC")
TestCase().assertEqual(string_expansion("23D42B3A"),"DDDBBAAA")
TestCase().assertEqual(string_expansion("143D36C1A"),"DDDCCCCCCA")
TestCase().assertEqual(string_expansion("asdf"),"asdf")
TestCase().assertEqual(string_expansion("23jbjl1eb"),"jjjbbbjjjllleb")
TestCase().assertEqual(string_expansion("43ibadsr3"),"iiibbbaaadddsssrrr")
TestCase().assertEqual(string_expansion("123p9cdbjs"),"pppcccccccccdddddddddbbbbbbbbbjjjjjjjjjsssssssss")
TestCase().assertEqual(string_expansion("2309ew7eh"),"eeeeeeeeewwwwwwwwweeeeeeehhhhhhh")
TestCase().assertEqual(string_expansion("312987rfebd"),"rrrrrrrfffffffeeeeeeebbbbbbbddddddd")
TestCase().assertEqual(string_expansion("126cgec"),"ccccccggggggeeeeeecccccc")
TestCase().assertEqual(string_expansion("1chwq3rfb"),"chwqrrrfffbbb")
TestCase().assertEqual(string_expansion("389fg21c"),"fffffffffgggggggggc")
TestCase().assertEqual(string_expansion("239vbsac"),"vvvvvvvvvbbbbbbbbbsssssssssaaaaaaaaaccccccccc")
TestCase().assertEqual(string_expansion("davhb327vuc"),"davhbvvvvvvvuuuuuuuccccccc")
TestCase().assertEqual(string_expansion("cvyb239bved2dv"),"cvybbbbbbbbbbvvvvvvvvveeeeeeeeedddddddddddvv")
TestCase().assertEqual(string_expansion(""),"")
# Mubashir