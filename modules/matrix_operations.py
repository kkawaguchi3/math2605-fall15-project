import numpy as np

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
    return np.zeros((np.shape(a)[0], np.shape(a)[1]))


def populate_diagonal(a):
    for i in range(0, np.shape(a)[0]):
        a[i, i] = 1
    return a


def lu_fact(a):
    """
    Implementation of LU factorization given a matrix A.
    Returns L, U, and the error.
    """
    shapeA = np.shape(a)

    # A must be a square matrix
    if (shapeA[0] != shapeA[1]):
        return None

    # start with matrix A, empty matrix U, and a partially complete matrix L
    u = get_empty_copy(a)
    l = get_empty_copy(a)
    # place 1's in L's diagonal
    populate_diagonal(l)
    # take the dot product of the first rows of L and A
    dot = np.dot(l[0], a)
    print(dot)
