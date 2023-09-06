def alpha_clash(str_A, ind_A, str_Z, ind_Z):
    str_A = [ord(l) for i, l in enumerate(str_A) if i not in ind_Z]
    str_Z = [ord(l) for i, l in enumerate(str_Z) if i not in ind_A]
    result = {"A": 0, "Z": 0}
    for a, z in zip(str_A, str_Z):
        if a - z > 0:
            result["A"] += a - z
        else:
            result["Z"] += abs(a - z)
    return result


print(alpha_clash(
    "MZNHUVIOEPTWFJCBXKALSDQGYR",
    [1, 3, 2, 8, 10, 12, 9, 7, 4, 22],
    "YFTUCSQOMGKPXNDWHIVJRABZEL",
    [21, 24, 25, 3, 4, 1, 8, 9, 10, 17]
))
