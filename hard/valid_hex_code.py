import re


def is_valid_hex_code(txt):
    return re.search("^#[\\dA-Fa-f]{6}$", txt) is not None


print(is_valid_hex_code("#CD5C5C"))
print(is_valid_hex_code("#CD5C58C"))
