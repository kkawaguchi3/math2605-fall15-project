import numpy as np
import matplotlib.pyplot as plt
import modules.matrix_operations as mo


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


print("\nnow I start solving problem")
# set E to 0.00005
E = 0.00005

# generates thousand of matrix
mat_list = mo.thousand_random_2x2_mats()



# computes (A^-1)
inverse_mat_list = []
for A in mat_list:
    inverse_mat_list.append(mo.find_2x2_mat_inverse(A))
print("\n")


print('making det_trace_iter\nAnd setting up coordinates for A')
det_list = []
trace_list = []
iter_list = []
for A in mat_list:
    det_trace_iter_tuple = mo.det_trace_iter(A, v, E)
    if det_trace_iter_tuple is not None:
        det_list.append(det_trace_iter_tuple[0])
        trace_list.append(det_trace_iter_tuple[1])
        iter_list.append(det_trace_iter_tuple[2])

print('making det_trace_iter\nAnd setting up coordinates for A')
inverse_mat_det_list = []
inverse_mat_trace_list = []
inverse_mat_iter_list = []
for A in inverse_mat_list:
    inv_det_trace_iter_tuple = mo.det_trace_iter(A, v, E)
    if inv_det_trace_iter_tuple is not None:
        inverse_mat_det_list.append(inv_det_trace_iter_tuple[0])
        inverse_mat_trace_list.append(inv_det_trace_iter_tuple[1])
        inverse_mat_iter_list.append(inv_det_trace_iter_tuple[2])


# graph for matrix A
plt.scatter(det_list, trace_list, c=iter_list)
plt.gray()
plt.title('Graph for A\nhigher the number of iteration, brighter the plot')
plt.xlabel('determinant')
plt.ylabel('trace')
plt.show()



# graph for A^-1
plt.scatter(inverse_mat_det_list, inverse_mat_trace_list, c=inverse_mat_iter_list)
plt.gray()
plt.title('Graph for A^-1\nhigher the number of iteration, brighter the plot')
plt.xlabel('determinant')
plt.ylabel('trace')
plt.show()