def dis(price, discount):
    return round(price * (1 - discount / 100), 2)


result = dis(89, 20)
print(result)
