"""
Atbash Cipher


The Atbash cipher is an encryption method in which each letter
of a word is replaced with its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.

Create a function that takes a string and applies the Atbash cipher to it.

Examples
atbash("apple") ➞ "zkkov"

atbash("Hello world!") ➞ "Svool dliow!"

atbash("Christmas is the 25th of December") ➞ "Xsirhgnzh rh gsv 25gs lu Wvxvnyvi"
Notes
Capitalisation should be retained.
Non-alphabetic characters should not be altered.


"""
from unittest import  TestCase


def atbash(text):
    atbash_dict = {chr(i): chr(122 - i + 97) for i in range(97, 123)}
    atbash_dict.update({chr(i): chr(90 - i + 65) for i in range(65, 91)})

    encoded_text = ''.join(atbash_dict.get(char, char) for char in text)

    return encoded_text


TestCase().assertEqual(atbash("abcdefghijklmnopqrstuvwxyz"), "zyxwvutsrqponmlkjihgfedcba")
TestCase().assertEqual(atbash("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), "ZYXWVUTSRQPONMLKJIHGFEDCBA")
TestCase().assertEqual(atbash("The word 'atbash' derives from the the first and last 2 letters of the Hebrew alphabet."), "Gsv dliw 'zgyzhs' wvirevh uiln gsv gsv urihg zmw ozhg 2 ovggvih lu gsv Svyivd zokszyvg.")
TestCase().assertEqual(atbash("Vmxibkgrlm zmw wvxibkgrlm ziv rwvmgrxzo uli gsv Zgyzhs xrksvi."),"Encryption and decryption are identical for the Atbash cipher.")