from textwrap import wrap


def rgb_or_hex(*args):
    if len(args) > 1:
        return "#" + "".join(["{:02x}".format(number) for number in args])
    else:
        args = args[0][1:]
        return tuple([int(s, 16) for s in wrap(args, 2)])


print(rgb_or_hex(150, 50, 76))
print(rgb_or_hex("#303749"))
print(rgb_or_hex(0, 0, 0))
