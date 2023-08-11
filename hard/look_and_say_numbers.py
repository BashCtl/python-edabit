import textwrap


def look_and_say(n):
    num = str(n)
    if len(num) % 2 != 0:
        return "invalid"
    pairs = textwrap.wrap(num, 2)
    return int("".join([pair[1] * int(pair[0]) for pair in pairs]))


# print(look_and_say(95))
print(look_and_say(1213141516171819))