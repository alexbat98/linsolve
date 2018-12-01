import numpy as np


def solve(a, b, epsilon=1e-5, max_iterations=100):
    n = a.shape[0]
    beta = np.zeros(n, dtype=np.float64)
    alpha = np.zeros((n, n), dtype=np.float64)

    for i in range(n):
        beta[i] = b[i] / a[i, i]

    for i in range(n):
        for j in range(n):
            if j != i:
                alpha[i, j] = - a[i, j] / a[i, i]

    x = beta.copy()
    x0 = beta.copy()
    for __ in range(max_iterations):
        x = beta + alpha.dot(x)
        if np.all(np.abs(x[i] - x0[i]) < epsilon for i in range(n)):
            return x
        x0 = x.copy()

    raise ValueError('Solution does not converge')
