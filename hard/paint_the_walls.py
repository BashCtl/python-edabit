import math


def time(dct, people, walls):
    per_people = dct["walls"] / (dct["people"] * dct["minutes"])
    return math.ceil(walls / (per_people * people))


rate = {
    "people": 10,
    "walls": 10,
    "minutes": 22
}

print(time(rate, 14, 14))
rate2 = {
  'people': 10,
  'walls': 10,
  'minutes': 22
}

print(time(rate2,10,10))