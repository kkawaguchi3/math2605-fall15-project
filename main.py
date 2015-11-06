#!/usr/bin/env python
import numpy as np
import modules.matrix_operations as mo

# testing matrix multiplication
matrixA = np.matrix([[1, 2], [2, 1], [2, 1]])
matrixB = np.matrix([[3, 2, 1], [2, 1, 1]])
answer = mo.matrix_multiply(matrixA, matrixB)
# print(answer)

# testing LU factorization
a = np.matrix([
                [2, -1, -2],
               [-4,  6,  3],
               [-4,  -2, 8]])
results = mo.lu_fact(a)
