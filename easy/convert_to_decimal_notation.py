def convert_to_decimal(perc):
    return list(map(lambda a: float(a.strip('%')) / 100, perc))


print(convert_to_decimal(["1%", "2%", "3%"]))
print(convert_to_decimal(["33%", "98.1%", "56.44%", "100%"]))


