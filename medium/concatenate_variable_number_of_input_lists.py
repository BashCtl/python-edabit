from itertools import chain


def concat(*args):
    return list(chain(*args))


print(concat([1, 2, 3], [4, 5], [6, 7]))