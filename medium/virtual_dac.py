def V_DAC(value):
    return round((value / 1023 * 5), 2)


print(V_DAC(0))
print(V_DAC(1023))
print(V_DAC(400))