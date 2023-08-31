import math


def id_mtrx(n):
    result = []
    try:
        index = 0 if n > 0 else abs(n) - 1
        r = abs(n)
        for x in range(r):
            inner = []
            for y in range(r):
                if y == index and 0 <= index < r:
                    inner.append(1)
                else:
                    inner.append(0)
            result.append(inner)
            if n > 0:
                index += 1
            else:
                index -= 1
    except TypeError:
        return "Error"
    return result


print(id_mtrx(2))
print(id_mtrx(-2))
print(id_mtrx(0))
print(id_mtrx("ddsf"))
