#!/usr/bin/env python
import numpy as np
import modules.problem1_operations as ops

#############
# Problem 1 #
#############
def print_something():
    print("IT WORKS")

# Part A
# ######
print("PART A\n========\n")
# testing LU factorization
a = np.matrix([
               [1, 1, 1, 1],
               [1, 2, 3, 4],
               [1, 3, 6, 10],
               [1, 4, 10, 20]])

# TODO: fix lu fact function
results = ops.lu_fact(a)
print("L:\n=====\n" + str(results[0]))
print("U:\n=====\n" + str(results[1]))
# test solving for LU
# TODO: implement lu solving

# Part B
# ######
print("PART B\n========\n")


# testing householder reflection
a = np.array(((
  (1, 1, 1, 1),
  (1, 2, 3, 4),
  (1, 3, 6, 10),
  (1, 4, 10, 20),
  )))

results = ops.qr_fact_househ(a)

print("Q:\n=====\n" + str(results[0]))
print("R:\n=====\n" + str(results[1]))
print("Error:\n=====\n" + str(results[2]))

# TODO: complete Givens rotation


# Part C
# ######
print("PART C\n========\n")

a = np.array(((

  (1, 1, 1, 1),
  (1, 2, 3, 4),
  (1, 3, 6, 10),
  (1, 4, 10, 20),
  )))

b = np.array((1, 1/2, 1/3, 1/4))

# 1
# #

# solve for Ax = b using QR decomposition
x, L, U, error = ops.solve_lu_b(a, b)

# 2
# #

# solve for Ax = b using QR decomposition
x, Q, R, error = ops.solve_qr_b(a, b)

print("x = \n" + str(x))

# Part D
# ######
print("PART D\n========\n")
