import numpy as np
import random as rand


# implementation of matrix multiplication method

def matrix_multiply(a, b):
    sizeA = np.shape(a)
    sizeB = np.shape(b)

    # check if inner and outer sizes will work
    if (sizeA[1] != sizeB[0]):
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


def power_method(A, v, E, N):
    """
    does power method
    """

    err = 0
    lamda = 0
    for i in range(0, N + 1):
        temp = matrix_multiply(A, v)
        newlamda = matrix_multiply(np.transpose(v), temp)[0, 0]
        newlamda = newlamda / matrix_multiply(np.transpose(v), v)[0, 0]

        # can we use magnitude method???
        err = np.absolute(newlamda - lamda)
        v = temp
        lamda = newlamda
    # does multiple multiplication for power method!!!
    u = np.transpose(v)
    if np.absolute(err) < np.absolute(lamda * E):
        return (v / (np.sqrt(matrix_multiply(u, v)[0, 0])), lamda)
    else:
        #print("Uhh, failed")
        return None
    # return v / (np.sqrt(matrix_multiply(u, v)[0, 0]))


# thousand 2x2 mat generator
def thousand_random_2x2_mats():
    """
    generates 1000 2x2 mats
    """
    i = 0
    mylist = []
    while i < 1000:
        randMat = np.matrix([[rand.uniform(-2, 2), rand.uniform(-2, 2)], [rand.uniform(-2, 2), rand.uniform(-2, 2)]])
        if randMat[0, 0] * randMat[1, 1] != randMat[0, 1] * randMat[1, 0]:
            mylist.insert(0, randMat)
            i = i + 1
        else:
            print("hmm")
    return mylist

# finds 2x2 inverse mat
def find_2x2_mat_inverse(imat):
    """
    creates inverse 2x2 mats for imat
    """
    imatDet = (imat[0, 0] * imat[1, 1] - imat[0, 1] * imat[1, 0])
    inverseMat = np.matrix([[imat[1, 1], -imat[0, 1]], [-imat[1, 0], imat[0, 0]]]) / imatDet
    return inverseMat

# returns trace
def trace(mat):
    """
    finds trace of the matrix
    """
    tracer = 0
    matshape = mat.shape
    if matshape[0] != matshape[1]:
        print(mat)
        print(matshape[0])
        print(matshape[1])
        print("Needs to be square mat!")
        return None
    for i in range(0, len(mat)):
        tracer = tracer + mat[i, i]
    return tracer


# estimate eigenvalue
def est_eigenvalues_2x2(A, v, E, N):
    """
    finds the big and small eigenvalues
    """
    # returns tuple(smallEigenvalue, bigEigenvalue)
    BIG_eigenvalue = power_method(A, v, E, N)[1]
    small_eigenvalue = power_method(find_2x2_mat_inverse(A), v, E, N)[1]
    return (small_eigenvalue, BIG_eigenvalue)

# find number of iterations needed and lamda found from there.
# def specific_tolerance_power_method(A, v, E):
#     """
#     :param A: input matrix
#     :param v: vector used for power method
#     :param E: tolerance parameter
#     :return: (N, lamda) -> N is number of iterations needed, lamda is largest abs value eigenvalue
#     """
#     N = 0;
#     while N <= 100:
#         N += 1
#         if power_method(A, v, E, N) is not None:
#             return N, power_method(A, v, E, N)[1]
#     return 100, None

def det_trace_iter(A, v, E):
    """
    :param A: input matrix
    :param v: vector used for power method
    :param E: tolerance parameter
    :return: (determinant, trace, N) ->determinant, trace, number of iterations
    """
    N = 0
    err = 0
    lamda = 0
    while np.absolute(err) >= np.absolute(lamda * E) and N <= 100:
        N += 1
        temp = matrix_multiply(A, v)
        newlamda = matrix_multiply(np.transpose(v), temp)[0, 0]
        newlamda = newlamda / matrix_multiply(np.transpose(v), v)[0, 0]

        # can we use magnitude method???
        err = np.absolute(newlamda - lamda)
        v = temp
        lamda = newlamda
    # does multiple multiplication for power method!!!
    if np.absolute(err) < np.absolute(lamda * E):
        return (determinant_for_2x2(A), trace(A), N)
    else:
        #print("Uhh, failed")
        return None


def determinant_for_2x2(A):
    if np.shape(A)[0] != 2 or np.shape(A)[1] != 2:
        print("Not correct dimension")
        return None
    return A[0, 0] * A[1, 1] - A[1, 0] * A[0, 1]


