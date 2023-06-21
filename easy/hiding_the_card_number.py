import re


def card_hide(card):
    return "*" * (len(card) - 4) + card[-4:]


print(card_hide("1234123456785678"))
