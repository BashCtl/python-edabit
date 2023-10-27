"""
Caesar Cipher

Create a function that takes two arguments (text, key)
and returns a new encrypted text using the key. For example,
if the input is "a" and the key is 1, it should move that
letter 1 step in alphabetic order so the output would be "b".

Examples
caesar_cipher("hello", 5) ➞ "mjqqt"

caesar_cipher("hello world", 1) ➞ "ifmmp xpsme"

caesar_cipher("a", 2) ➞ "c"

Notes
The input is only letters and spaces; no special characters.

"""


def caesar_cipher(text, key):
    result = []
    for char in text:
        if char.isalpha():
            if ord(char) + key <= ord('z'):
                result.append(chr(ord(char) + key))
            else:
                result.append(chr(ord(char) + key-ord('z')+ord('a')-1))
        else:
            result.append(char)

    return "".join(result)


print(caesar_cipher("hello", 5))
print(caesar_cipher("hello world", 1))
print(caesar_cipher("hello world", 26))
print(caesar_cipher("a", 2))
