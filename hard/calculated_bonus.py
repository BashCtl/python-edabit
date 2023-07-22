def bonus(days):
    total = 0
    if days > 48:
        total += (days - 48) * 600
        days = 48
    if days > 40:
        total += (days - 40) * 550
        days = 40
    if days > 32:
        total += (days - 32) * 325
    return total


print(bonus(15))
print(bonus(37))
print(bonus(50))
