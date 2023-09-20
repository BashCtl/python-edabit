import numpy as np


def matrix_mult(m1, m2):
    m1 = np.array(m1)
    m2 = np.array(m2)
    inner = []
    result = []
    for row in m1:
        for i in range(2):
            item = sum([x * y for x, y in zip(row, m2[:, i])])
            inner.append(item)
        result.append(inner)
        inner = []
    return result


print(matrix_mult([[4, 2],
                   [3, 1]],
                  [[5, 6],
                   [3, 8]]))
