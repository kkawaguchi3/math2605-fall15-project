import numpy as np
import matplotlib.pyplot as plt
import modules.matrix_operations as mo


# test power method & v = (1, 1)
A = np.matrix([[2, -12], [1, -5]])
v = np.matrix([[1],[1]])

# First array is the eigenvector, second is corresponding eigenvalue float
print('NOTE: All the power method and related methods are in the modules.matrix_operations')
print('Let\'s test Power Method power_method(A, v, E, N\nsuppose we use tolerance of 0.01 and 6 iteration limit')
print('we will use matrix A')
print('Note that power method returns a tuple with (eigenvector, eigenvalue)')
print(A)
print('and vector (1, 1)')
powerAns = mo.power_method(A, v, .01, 6)
print(powerAns)
print('But if we change the iteration to 5\nresult will fail and return None')
print(mo.power_method(A, v, .01, 5))
print('Hey, it can do power method for 3 by 3 mat!')
print('Our new mat is below, everything else same')
Three = np.matrix([[1, 2, 0], [-2, 1, 2], [1, 3, 1]])
print(Three)
powerAns_3x3 = mo.power_method(A, v, .01, 6)
print(powerAns_3x3)
print('Wow and then let\'s get 3rd mat from thousands of random matrices')
print(mo.thousand_random_2x2_mats()[3])
print('\n')
c = np.matrix([
               [2, 1],
               [1, 2]])
print(c)
print('is our test Mat C')
print('C^-1')
print(mo.find_2x2_mat_inverse(c))
print('C^-1 * C')
print(mo.matrix_multiply(mo.find_2x2_mat_inverse(c), c))
print('tr(C) = ')
print(mo.trace(c))
print('Two eigenvalue approximation with v = (1, 1), E = 0.01, N = 6')
print(mo.est_eigenvalues_2x2(A, v, .01, 6))
print('\n\n')


print("\nnow I start solving problems for b ~ c.\nGraphs should show up by order\nclose a Graph to see next Graph")
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
#plt.gray()
plt.title('Graph for A\nhigher the number of iteration, brighter the plot')
plt.xlabel('determinant')
plt.ylabel('trace')
plt.colorbar(plt.gray()).set_label('Number of Iterations')
plt.show()



# graph for A^-1
plt.scatter(inverse_mat_det_list, inverse_mat_trace_list, c=inverse_mat_iter_list)
#plt.gray()
plt.title('Graph for A^-1\nhigher the number of iteration, brighter the plot')
plt.xlabel('determinant')
plt.ylabel('trace')
plt.colorbar(plt.gray()).set_label('Number of Iterations')
plt.show()