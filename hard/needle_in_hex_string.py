# def first_index(hex_txt, needle):
#     needle = needle.encode("utf-8").hex()
#     for i, h in enumerate(hex_txt.split(" ")):
#         if needle.startswith(h):
#             return i


import binascii


def first_index(hex_txt, needle):
    needle = needle.encode("utf-8")
    hex_value = binascii.hexlify(needle).decode("utf-8")
    for i, h in enumerate(hex_txt.split(" ")):
        if hex_value.startswith(h):
            return i


print(first_index("68 65 6c 6c 6f 20 77 6f 72 6c 64", "world"))
print(first_index("47 6f 6f 64 62 79 65 20 77 6f 72 6c 64", "world"))
print(first_index("42 6f 72 65 64 20 77 6f 72 6c 64", "Bored"))
