def num_layers(n):
    meters = (0.5 * (2 ** n)) / 1000
    return "{}m".format(meters)


print(num_layers(1))
print(num_layers(4))
print(num_layers(21))
