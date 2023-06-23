import re


def dna_to_rna(dna):
    dna = re.sub("A", "U", dna)
    dna = re.sub("T", "A", dna)
    dna = re.sub("G", "X", dna)
    dna = re.sub("C", "G", dna)
    dna = re.sub("X", "C", dna)
    return dna


print(dna_to_rna("ATTAGCGCGATATACGCGTAC"))
