import numpy as np


def solve(matrix, b):
    for c in range(0, len(b)):
        mult = matrix[c, c]
        for x in range(0, len(b)):
            matrix[c, x] = matrix[c, x] / mult

        b[c] = b[c] / mult

        for y in range(c+1, len(b)):
            mult = matrix[y, c]
            b[y] -= mult * b[c]

            for x in range(0, len(b)):
                matrix[y, x] -= mult * matrix[c, x]

    x = np.zeros(len(b), dtype=np.float64)
    x[len(b) - 1] = b[len(b) - 1]

    for y in range(len(b) - 2, -1, -1):
        x[y] = b[y]
        for i in range(len(b) - 1, y, -1):
            x[y] -= x[i]*matrix[y, i]

    return x
