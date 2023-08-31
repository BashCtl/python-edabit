from fractions import Fraction


def simplify(txt):
    numbers = [int(i) for i in txt.split("/")]
    return str(Fraction(numbers[0], numbers[1]))


print(simplify("4/6"))
print(simplify("100/400"))
