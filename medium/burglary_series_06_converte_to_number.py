def convert_to_number(dictionary):
    return {k: int(v) for k, v in dictionary.items()}


print(convert_to_number({"piano": "200", "tv": "300"}))
