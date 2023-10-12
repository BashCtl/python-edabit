import re


def simple_symbols(txt):
    pattern = r"(?<=\+)[a-z](?=\+)"
    return len(re.findall(pattern, txt)) == len(re.sub("[^a-z]", "", txt))


print(simple_symbols("==+p+++++++++====8+z++++"))
print(simple_symbols("f++d+"))
print(simple_symbols("======2+++4+u===+i+"))
