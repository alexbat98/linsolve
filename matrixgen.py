import numpy as np
import random


class MatrixGenerator:
    @staticmethod
    def generate_matrix(size):
        matrix = np.zeros((size, size), dtype=np.float64)
        for x in range(0, size):
            for y in range(0, size):
                matrix[y, x] = random.random() * 1000
        s = np.sum(np.abs(matrix), axis=1)
        for x in range(0, size):
            matrix[x, x] = s[x] + random.random() * 1000
        return matrix

    @staticmethod
    def generate_b(size):
        b = np.zeros(size, dtype=np.float64)
        for x in range(0, size):
            b[x] = random.random() * 1000
        return b
