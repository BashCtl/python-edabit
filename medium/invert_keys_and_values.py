def invert(dct):
    return {v: k for k, v in dct.items()}


print(invert({"z": "q", "w": "f"}))
