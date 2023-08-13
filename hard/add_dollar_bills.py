import re


def add_bill(money):
    money = list(filter(None,re.sub(r"p\d{1,}[,k]?|[d]", "", money).split(",")))
    return sum([int(price) if "k" not in price else int(price.replace("k", "")) * 1000
                for price in money])


# print(add_bill("d20,p40,p60,d50"))
# print(add_bill("d200,p40,p60,d1k"))
# print(add_bill("d10k,p500,p200"))
print(add_bill("p20k,p100,d100"))