#!/usr/bin/env python
import numpy as np
import modules.matrix_operations as mo
import matplotlib.pyplot as plt


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

# test power method & v = (1, 1)
A = np.matrix([[2, -12], [1, -5]])
v = np.matrix([[1],[1]])
powerAns = mo.power_method(A, v, .01, 6)
# First array is the eigenvector, second is corresponding eigenvalue float
print(powerAns)
print(mo.thousand_random_2x2_mats()[3])
c = np.matrix([
               [2, 1],
               [1, 2]])
print(mo.find_2x2_mat_inverse(c))
print(mo.matrix_multiply(mo.find_2x2_mat_inverse(c), c))
print(mo.trace(c))
print(mo.est_eigenvalues_2x2(A, v, .01, 6))
print("This is 3.b")
print(mo.specific_tolerance_power_method(A, v, .01))

print("\nnow I start solving problem")
# set E to 0.00005
E = 0.00005

# generates thousand of matrix
mat_list = mo.thousand_random_2x2_mats()
print("A")
print(mat_list[2])
print("\n")


# computes (A^-1)
inverse_mat_list = []
for A in mat_list:
    inverse_mat_list.append(mo.find_2x2_mat_inverse(A))
print("A^-1")
print(inverse_mat_list[2])
print("\n")
#
#
# # do power method to find largest eigenvalue of A within E = 0.00005
iter_list = []
print("wait for 5~6 min")
for A in mat_list:
    iter_list.append(mo.specific_tolerance_power_method(A, v, E)[0])

print("\n")
# #
# # do same for A^-1
inverse_mat_iter_list = []
for A in inverse_mat_list:
    inverse_mat_iter_list.append(mo.specific_tolerance_power_method(A, v, E)[0])

print("\n")

#
# record the trace and determinant of A & A^-1


determinant_list = []
for A in mat_list:
    determinant_list.append(mo.determinant_for_2x2(A))
print("deteminant of A")
print(determinant_list[2])
print("\n")

#
inverse_mat_determinant_list = []
for A in inverse_mat_list:
    inverse_mat_determinant_list.append(mo.determinant_for_2x2(A))
print("deteminant of A^-1")
print(inverse_mat_determinant_list[2])
print("\n")


trace_list = []
for A in mat_list:
    trace_list.append(mo.trace(A))
print("trace of A")
print(trace_list[2])
print("\n")


inverse_mat_trace_list = []
for A in inverse_mat_list:
    inverse_mat_trace_list.append(mo.trace(A))
print("trace of A^-1")
print(inverse_mat_trace_list[2])


# graph for matrix A
plt.scatter(determinant_list, trace_list, c=iter_list)
plt.gray()
plt.title('Graph for A\nhigher the number of iteration, brighter the plot')
plt.xlabel('deteminant')
plt.ylabel('trace')
plt.show()



# graph for A^-1
plt.scatter(inverse_mat_determinant_list, inverse_mat_trace_list, c=iter_list)
plt.gray()
plt.title('Graph for A^-1\nhigher the number of iteration, brighter the plot')
plt.xlabel('deteminant')
plt.ylabel('trace')
plt.show()