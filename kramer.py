import numpy as np


def det(matrix):
    for c in range(0, len(matrix[0])):
        for y in range(c+1, len(matrix[0])):
            mult = matrix[y, c]
            div = matrix[c, c]

            for x in range(0, len(matrix[0])):
                matrix[y, x] -= mult * matrix[c, x] / div

    det_res = 1
    for c in range(0, len(matrix[0])):
        det_res *= matrix[c, c]

    return det_res


def solve(matrix, b):
    m = np.copy(matrix)
    delta = det(m)

    deltas = np.zeros(len(b), dtype=np.float64)

    for i in range(0, len(b)):
        m = np.copy(matrix)
        for j in range(0, len(b)):
            m[j, i] = b[j]
        deltas[i] = det(m)

    x = np.zeros(len(b), np.float64)
    for i in range(len(b)):
        x[i] = deltas[i] / delta

    return x
