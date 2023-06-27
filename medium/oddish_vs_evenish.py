def oddish_or_evenish(num):
    number = sum([int(n) for n in str(num)])
    return "Evenish" if number % 2 == 0 else "Oddish"


print(oddish_or_evenish(43))
print(oddish_or_evenish(4433))