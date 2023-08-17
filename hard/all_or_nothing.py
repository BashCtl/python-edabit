def possibly_perfect(key, answers):
    return (all([k == a or k == "_" for k, a in zip(key, answers)])
            or all([k != a for k, a in zip(key, answers)]))


print(possibly_perfect(["B", "A", "_", "_"],
                       ["B", "A", "C", "C"]))
print(possibly_perfect(["A", "B", "A", "_"],
                       ["B", "A", "C", "C"]))
print(possibly_perfect(["A", "B", "C", "_"],
                       ["B", "A", "C", "C"]))