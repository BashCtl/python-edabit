import re


def is_valid_PIN(pin):
    if re.search(r"^(\d{4}|\d{6})$", pin):
        return True
    return False


print(is_valid_PIN("1234"))
print(is_valid_PIN("12345"))
print(is_valid_PIN("a234"))
print(is_valid_PIN(""))
