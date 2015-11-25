#!/usr/bin/env python
import numpy as np
import modules.matrix_operations as mo
import modules.iterativeMethods as im
import matplotlib.pyplot as plt

# Part 2
im.jacobi_iter()

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
b = np.matrix([
               [1, 1, 1, 1],
               [1, 2, 3, 4],
               [1, 3, 6, 10],
               [1, 4, 10, 20]])
results = mo.lu_fact(b)




