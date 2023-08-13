import textwrap


def split_n_cases(txt, cases):
    if len(txt) % cases == 0:
        return textwrap.wrap(txt, len(txt) // cases)
    return ["Error"]


print(split_n_cases("Strengthened", 6))
print(split_n_cases("Fool's Errand", 20))
