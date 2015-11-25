import numpy as np
import math
# implementation of matrix multiplication method


def matrix_multiply(a, b):
    sizeA = np.shape(a)
    sizeB = np.shape(b)

    # check if inner and outer sizes will work
    if(sizeA[1] != sizeB[0]):
        return None

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
    print(n)
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
    product = M_1 * M_2 - A
    norm = np.linalg.norm(product)
    return norm


def solve_lu_b(L, U, P, b):
    x = U/(L/(np.transpose(P) * b))
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


def least_square(a, b, q, r):
    _, n = r.shape
    return np.linalg.solve(r[:n, :], np.dot(q.T, b)[:n])


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


def part_d_setup():
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
        x, Q, R, error = solve_qr_b(P, b)
    # output solution x_sol
        print("case n = " + str(n))
        print("x_sol:\n" + str(x))
        print("error:\n" + str(error))
    # output the errors: lu_minus_p, qr_minus_p, px_sol_minus b


# Summarize your findings by plotting the errors obtained as a function of n, for each
# of the methods. The plot can be done using your own code, Excel, or any graphing
# program. The plots should be included in the written component of this part of the
# project.


## Section for testing

part_d_setup()