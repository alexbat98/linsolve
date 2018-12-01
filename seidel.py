import numpy as np


def solve(m, b, x0=None, eps=1e-5, max_iteration=100):
    n = m.shape[0]
    x0 = np.zeros(n, dtype=np.float32) if x0 is None else x0
    x1 = x0.copy()

    for __ in range(max_iteration):
        for i in range(n):
            s = sum(-m[i, j] * x1[j] for j in range(n) if i != j)
            x1[i] = (b[i] + s) / m[i][i]
        if all(abs(x1[i] - x0[i]) < eps for i in range(n)):
            return x1
        x0 = x1.copy()
    raise ValueError('Solution does not converge')
