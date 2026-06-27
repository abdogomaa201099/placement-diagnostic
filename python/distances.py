# Task 3: Vectorized Pairwise Distances. See ../python.md for the full task.
# Complete the fast function below, then run this file:  python distances.py
# It should print:  Match: True

import numpy as np


def slow(a, b):
    # Reference implementation — do NOT modify.
    n, m = len(a), len(b)
    out = [[0.0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            total = 0.0
            for k in range(len(a[i])):
                diff = a[i][k] - b[j][k]
                total += diff * diff
            out[i][j] = total
    return out


def fast(a, b):
    # TODO: return the same result as slow(a, b), using only NumPy operations
    # here — no for loops or list comprehensions.
    #raise NotImplementedError("Implement fast() using NumPy broadcasting.")
    res1 = np.pow(abs(a - b[0, :]), 2)
    res2 = np.pow(abs(a - b[1, :]), 2)
    # print(res1)
    # print(res2)
    res3 = res1[:, 0] + res1[:, 1]
    res4 = res2[:, 0] + res2[:, 1]
    # print(res3)
    # print(res4)
    res = np.array([res3,res4]).T
    print(res)
    return res
if __name__ == "__main__":
    a = np.array([[0, 0], [3, 4], [1, 2]])
    b = np.array([[0, 0], [1, 1]])


    print("Match:", np.allclose(np.array(slow(a, b)), fast(a, b)))