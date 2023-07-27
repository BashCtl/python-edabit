import re


def parse_code(txt):
    values = re.split("[0]{1,}", txt)
    return {
        "first_name": values[0],
        "last_name": values[1],
        "id": values[2]
    }


print(parse_code("John000Doe000123"))
