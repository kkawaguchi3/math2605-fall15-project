import numpy as np
import math
import csv

# implementation of matrix multiplication method


def matrix_multiply(a, b):
    sizeA = np.shape(a)
    sizeB = np.shape(b)

    # check if inner and outer sizes will work
    if(sizeA[1] != sizeB[0]):
        return None
    print(sizeB)
    iMax = sizeA[0]  # index i is contained by the # of rows of A
    jMax = sizeB[1]  # index j is contained by the # of cols of B
    numRowsB = sizeB[0]
    rangeI = range(0, iMax)
    rangeJ = range(0, jMax)
    rangeK = range(0, numRowsB)

    # iterate through the matrix and apply matrix multiplicatin logic
    newMatrix = np.zeros((iMax, jMax))
    for i in rangeI:

        for j in rangeJ:
            for k in rangeK:
                newMatrix[i, j] += a[i, k] * b[k, j]
    return newMatrix


def get_empty_copy(a):
    """creates an empty array matching the size of matrix argument"""
    return np.matrix(np.zeros((np.shape(a)[0], np.shape(a)[1])))


def populate_diagonal(a):
    for i in range(0, np.shape(a)[0]):
        a[i, i] = 1
    return a


def calculate_u_position(u, a, l, i, n):
    # assigning values to row i of U
    for j in range(i, n):
        u[i, j] = a[i, j]
        # do a dot product
        for k in range(0, i):
            u[i, j] = u[i, j] - l[i, k] * u[k, j]


def calculate_l_position(u, a, l, i, n):
    # assigning values to column i of L
    for j in range(i + 1, n):
        l[j, i] = a[j, i]
        # do a dot product
        for k in range(0, i):
            l[j, i] = (l[j, i] - l[j, k] * u[k, i])
        l[j, i] = l[j, i] / u[i, i]


def lu_fact(a):
    """
    Implementation of LU factorization given a matrix A.
    Returns L, U, and the error.
    """
    shapeA = np.shape(a)

    # A must be a square matrix
    if (shapeA[0] != shapeA[1]):
        return None
    n = shapeA[0]
    # start with matrix A, empty matrix U, and a partially complete matrix L
    u = get_empty_copy(a)
    l = get_empty_copy(a)
    # place 1's in L's diagonal
    populate_diagonal(l)
    # the loop where interesting stuff happens
    for i in range(0, n):
        # looking at the first half of A
        calculate_u_position(u, a, l, i, n)
        calculate_l_position(u, a, l, i, n)
    # now L and U have been formed
    error = calc_error(l, u, a)
    return l, u, error


def calc_error(M_1, M_2, A):
    product = (np.dot(M_1, M_2)) - A
    # product = (M_1 * M_2) - A
    norm = calc_norm(product)
    return norm


def calc_norm(a):
    norm = np.absolute(np.max(a))
    return norm


def solve_lu_b(A, b):
    L, U, error = lu_fact(A)
    print(L)
    print(U)
    # x = U\(L\(P'*b))
    # first find (L\(P'*b))
    x = forward_sub(L, (np.dot(A.T, b)))
    # x is close enough, no back substitution necessary for Pascals
    return x, L, U, error


def forward_sub(A, b_orig):
    b = np.copy(b_orig)
    n = A.shape[0]
    x = np.zeros_like(b)
    x[0] = b[0] / A[0, 0]
    for i in range(0, n):
        print("i " + str(i))
        x[i] = (b[i] - np.dot(A[i, :i].flatten(), x[:i]))
        print(x)
    return x


def qr_fact_househ(A):

    a_row = np.shape(A)[0]
    a_col = np.shape(A)[1]
    Q = np.eye(a_row)
    R = A.copy()
    for i in range(a_col - (a_row == a_col)):
        H = np.eye(a_row)
        H[i:, i:] = householder(R[i:, i])
        Q = np.dot(Q, H)
        R = np.dot(H, R)
    error = calc_error(Q, R, A)
    return Q, R, error


def householder(a):
    v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    v[0] = 1
    H = np.eye(a.shape[0])
    H -= (2 / np.dot(v, v)) * np.dot(v[:, None], v[None, :])
    return H

def qr_fact_givens(A_orig):
    # select the correct givens positions
    #A = np.matrix([[1., 2., 3.], [-1., 3., 4.], [2., 5., 6.]])
    A = np.copy(A_orig)
    m, n = np.shape(A)
    if (m > n):
        k = n
    elif (m == n):
        k = n - 1
    else:
        k = m - 1
    # let Q be I = in size to A
    Q = np.eye(m)
    # begin givens calculations
    for j in range(0, k):
        for i in range(j + 1, m):
            G = givens(A[j,j], A[i, j])
            temp = A[j, :]
            temp = np.vstack([temp, A[i, :]])
            temp = np.dot(G, temp)
            A[j,:] = temp[0]
            A[i, :] = temp[1]
            # now for Q
            temp = Q[j, :]
            temp = np.vstack([temp, Q[i, :]])
            temp = np.dot(G, temp)
            Q[j,:] = temp[0]
            Q[i, :] = temp[1]
    error = calc_error(Q, A, A_orig)
    return Q, A, error


def givens(entry1, entry2):
    if (int(entry1) == 0 & int(entry2) == 0):
        G = np.eye(2)
    elif (np.absolute(entry2) >= np.absolute(entry1)):
        t = entry1 / entry2
        s = 1 / np.sqrt(1 + np.power(t, 2))
        c = s * t
        G = np.matrix([[c, s], [-s, c]])
    else:
        t = entry2 / entry1
        c = 1 / np.sqrt(1 + np.power(t, 2))
        s = c * t
        G = np.matrix([[c, s], [-s, c]])
    return G


def least_square(a, b, q, r):
    _, n = r.shape
    # x = R\(R'\(A'*b));
    return np.linalg.solve(r[:n, :], np.dot(q.T, b)[:n])


def solve_qr_b_givens(A, b):
    Q, R, error = qr_fact_givens(A)
    x = least_square(A, b, Q, R)
    return x, Q, R, error

def solve_qr_b(A, b):
    Q, R, error = qr_fact_househ(A)
    x = least_square(A, b, Q, R)
    return x, Q, R, error


def create_pascal(n):
    # P is nxn matrix
    P = np.ones((n, n))
    for i in range(0, n):
        for j in range(0, n):
            pascal_entry = math.factorial((i) + (j))
            pascal_entry /= (math.factorial(i) * math.factorial(j))
            P[i, j] = pascal_entry
    return P


def create_b(n):
    b = np.zeros((n))
    for i in range(0, n):
        b[i] = (1 / (i+1))
    return b


def part_d_qr_givens():
    data = []
    data.append(['n', 'operation_error', 'solution_error'])

    # for each n = 2: 12
    for n in range(2, 12):
        # solve the system Px = b
        P = create_pascal(n)
        # b = (1, 1/2, ... , 1/n)^t
        b = create_b(n)
        # use both lu_solve and qr_solve
        # QR householder
        x, Q, R, error = solve_qr_b_givens(P, b)
        sol_error = calc_error(P, x, b)
    # output solution x_sol
        print("-----------------")
        print("case n = " + str(n) + "\n-----------------")
        print("x_sol:\n" + str(x))
    # output the errors: lu_minus_p, qr_minus_p, px_sol_minus b
        print("operational error:\n" + str(error))
        print("solution error:\n" + str(sol_error))
        # save results to list
        data.append([n, error, sol_error])
    return data


def part_d_qr():
    data = []
    data.append(['n', 'operation_error', 'solution_error'])

    # for each n = 2: 12
    for n in range(2, 12):
        # solve the system Px = b
        P = create_pascal(n)
        # b = (1, 1/2, ... , 1/n)^t
        b = create_b(n)
        # use both lu_solve and qr_solve
        # QR householder
        x, Q, R, error = solve_qr_b(P, b)
        sol_error = calc_error(P, x, b)
    # output solution x_sol
        print("-----------------")
        print("case n = " + str(n) + "\n-----------------")
        print("x_sol:\n" + str(x))
    # output the errors: lu_minus_p, qr_minus_p, px_sol_minus b
        print("operational error:\n" + str(error))
        print("solution error:\n" + str(sol_error))
        # save results to list
        data.append([n, error, sol_error])
    return data


def part_d_lu():
    data = []
    data.append(['n', 'operation_error', 'solution_error'])

    # for each n = 2: 12
    for n in range(2, 12):
        # solve the system Px = b
        P = create_pascal(n)
        # b = (1, 1/2, ... , 1/n)^t
        b = create_b(n)
        # use both lu_solve and qr_solve
        # TODO: solve using lu
        # TODO: solve using givens
        # QR householder
        x, L, U, error = solve_lu_b(P, b)
        sol_error = calc_error(P, x, b)
    # output solution x_sol
        print("-----------------")
        print("case n = " + str(n) + "\n-----------------")
        print("x_sol:\n" + str(x))
    # output the errors: lu_minus_p, qr_minus_p, px_sol_minus b
        print("operational error:\n" + str(error))
        print("solution error:\n" + str(sol_error))
        # save results to list
        data.append([n, error, sol_error])
    return data

def save_to_csv(file_name, aList):
    with open(file_name, 'w', newline='') as myfile:
        writer = csv.writer(myfile)
        writer.writerows(aList)


#test norms
a = np.array(((
  (1, 1, 1, 1),
  (1, 2, 3, 4),
  (1, 3, 6, 10),
  (1, 4, 10, 20),
  )))

b = np.array((1, 1/2, 1/3, 1/4))

# lu_data = part_d_lu()
# save_to_csv('../lu_error_data.csv', lu_data)

#qr_data = part_d_qr()
#save_to_csv('../qr_error_data.csv', qr_data)
#
#results = solve_lu_b(a, b)
# 
# results = solve_qr_b(create_pascal(10), create_b(10))
# results = qr_fact_givens(create_pascal(4))
# print(results[0])
# print(results[1])
# print(results[2])
data = part_d_qr_givens()