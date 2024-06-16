"""
Morse Code Decoded
Create a function that takes a string (morse code) as an argument and returns an unencrypted string.

Examples
decode_morse(".... . .-.. .--.   -- .   -.-.--") ➞ "HELP ME !"

decode_morse("-.-. .... .- .-.. .-.. . -. --. .") ➞ "CHALLENGE"

decode_morse(". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. .") ➞ "EDABBIT CHALLENGE"
The following dict can be used for coding:

morse_to_dots = {
  "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
  "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
  "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
  "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
  "Y": "-.--", "Z": "--..", "0": "-----",
  "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
  "6": "-....", "7": "--...", "8": "---..", "9": "----.",
  "&": ".-...", "'": ".----.", "@": ".--.-.", ")": "-.--.-", "(": "-.--.",
  ":": "---...", ",": "--..--", "=": "-...-", "!": "-.-.--", ".": ".-.-.-",
  "-": "-....-", "+": ".-.-.", '"': ".-..-.", "?": "..--..", "/": "-..-."
}

dots_to_morse = {}
for key, val in morse_to_dots.items():
    dots_to_morse[val] = key
Notes
Return values are all uppercase.
Input string can have digits.
Input string can have some special chararacters (e.g. comma, colon, apostrophe, period, question mark, exclamation mark).

"""

from unittest import TestCase
import re

morse_to_dots = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..", "0": "-----",
    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
    "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    "&": ".-...", "'": ".----.", "@": ".--.-.", ")": "-.--.-", "(": "-.--.",
    ":": "---...", ",": "--..--", "=": "-...-", "!": "-.-.--", ".": ".-.-.-",
    "-": "-....-", "+": ".-.-.", '"': ".-..-.", "?": "..--..", "/": "-..-."
}

dots_to_morse = {}
for key, val in morse_to_dots.items():
    dots_to_morse[val] = key


def decode_morse(s):
    result = "".join([dots_to_morse[k] if k else " " for k in s.split(" ")])
    return re.sub(r"\s+", " ", result)


TestCase().assertEqual(decode_morse(". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."), "EDABBIT CHALLENGE")
TestCase().assertEqual(decode_morse(".... . .-.. .--.   -- .   -.-.--"), "HELP ME !")
TestCase().assertEqual(decode_morse("-.-. .... .- .-.. .-.. . -. --. ."), "CHALLENGE")
TestCase().assertEqual(decode_morse(
    ".----   .- .--. .--. .-.. .   .- -. -..   .....   -.-. .... . .-. .-. -.-- --..--   --...   ... .- -. -.. .-- .. -.-. .... . ... --..--   ..---   - .- -... .-.. . ... --..--   ----.   .. -. ...- .. - . -..   --. ..- -.-- ...   -.-.--   - .... .- - .----. ...   ... ---   -.-. --- --- .-.. .-.-.- .-.-.- .-.-.-"),
                       "1 APPLE AND 5 CHERRY, 7 SANDWICHES, 2 TABLES, 9 INVITED GUYS ! THAT'S SO COOL...")
TestCase().assertEqual(decode_morse("-.. .. -..   -.-- --- ..-   --. --- -   -- -.--   -- .- .. .-..   ..--.."),
                       "DID YOU GOT MY MAIL ?")
TestCase().assertEqual(decode_morse(
    "- .-- ---   - .... .. -. --. ...   - ---   -.- -. --- .--   ---...   ..   ..-. --- .-. --. . -   - .... . --   ---... -.-."),
                       "TWO THINGS TO KNOW : I FORGET THEM :C")
