import binascii


def convert_to_hex(txt):
    return " ".join([hex(ord(l))[2:] for l in txt])


print(convert_to_hex("hello world"))
