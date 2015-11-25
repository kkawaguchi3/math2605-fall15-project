import numpy as np
import random
import math
import numpy.matlib
import csv

# get diagonal matrix
def get_diagonal(x):
    sizeA = np.shape(x)
    iMax = sizeA[0]
    jMax = sizeA[1]

    newMatrix = np.zeros((iMax, jMax))

    rangei = range(0, 3)
    rangej = range(0, 3)

    for i in rangei:

        for j in rangej:
            if (i == j):
                newMatrix[i, j] += x[i, j]

    return newMatrix


def get_upper(x):
    sizeA = np.shape(x)
    iMax = sizeA[0]
    jMax = sizeA[1]

    newMatrix = np.zeros((iMax, jMax))

    for i in range(0, 3):
        for j in range(0, 3):

            if i == 0 and j > 0:
                newMatrix[i, j] += x[i, j]
            if i == 1 and j > 1:
                newMatrix[i, j] += x[i, j]

    return newMatrix


def get_lower(x):
    sizeA = np.shape(x)
    iMax = sizeA[0]
    jMax = sizeA[1]

    newMatrix = np.zeros((iMax, jMax))

    for i in range(0, 3):
        for j in range(0, 3):

            if i > 0 and j == 0:
                newMatrix[i, j] += x[i, j]
            if i > 1 and j == 1:
                newMatrix[i, j] += x[i, j]

    return newMatrix


def random_three_by_matrix():
    newMatrix = np.zeros((3, 1))
    newMatrix[0][0] = random.uniform(-1, 1)
    newMatrix[1][0] = random.uniform(-1, 1)
    newMatrix[2][0] = random.uniform(-1, 1)

    return newMatrix


def get_inverse(x):
    sizeA = np.shape(x)
    iMax = 3
    jMax = 3

    newMatrix = np.zeros((iMax, jMax), dtype=object)

    rangei = range(0, iMax)
    rangej = range(0, jMax)

    a = 0
    b = 0
    d = 0
    e = 0
    c = 0
    f = 0

    for i in rangei:

        for j in rangej:

            if i == 0 and j == 0:
                a = x[i, j]

            if i == 1 and j == 0:
                b = x[i, j]

            if i == 2 and j == 0:
                d = x[i, j]

            if i == 1 and j == 1:
                c = x[i, j]

            if i == 2 and j == 1:
                e = x[i, j]

            if i == 2 and j == 2:
                f = x[i, j]

    for i in rangei:

        for j in rangej:

            if i == 0 and j == 0:
                newMatrix[i, j] = 1 / a

            if i == 1 and j == 0:
                value1 = (-b / (a * c))
                newMatrix[i, j] = value1

            if i == 2 and j == 0:
                value2 = (((-c * d) + (b * e)) / (a * c * f))
                newMatrix[i, j] = value2

            if i == 1 and j == 1:
                value3 = (1 / c)
                newMatrix[i, j] = value3

            if i == 2 and j == 1:
                value4 = (-e / (c * f))

                newMatrix[i, j] = value4

            if i == 2 and j == 2:
                value5 = 1 / f

                newMatrix[i, j] = value5

    return newMatrix


# matrix multiply
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


# compute norm of matrix
def norm(x, x1):
    # a = x.transpose()
    # b = x1
    B = x - x1


    return math.sqrt(max(matrix_multiply(B.transpose(), B)))


def jacobi_iter(a, b, x, M, E):
    new_x = x
    old_x = x
    diagonal = get_inverse(get_diagonal(a))
    left = get_lower(a)
    upper = get_upper(a)

    lower_plus_upper = left + upper
    counter = 0
    for counter in range(M):
        new_x = matrix_multiply(diagonal, (matrix_multiply(-lower_plus_upper, new_x) + b))
        if (norm(new_x, old_x) < E):
            return (counter + 1, new_x)
        old_x  = new_x


def gs_iter(a, b, x, M, E):
    new_x = x
    old_x = x
    lower = get_lower(a)
    diagonal = get_diagonal(a)
    upper = get_upper(a)
    new_x = random_three_by_matrix()
    lower_inverse = get_lower(a)
    counter = 0
    inverse_ld = get_inverse(diagonal - lower)
    for counter in range(M):
        new_x = matrix_multiply(inverse_ld, (matrix_multiply(upper, new_x) + b))
        if (norm(new_x, old_x) < E):
            return (counter + 1, new_x)
        old_x = new_x



# test files

s = np.matrix(([1, 1 / 2, 1 / 3],
               [1 / 2, 1, 1 / 4],
               [1 / 3, 1 / 4, 1]))

d = np.matrix(([0.1],
               [0.1],
               [0.1]))
x_realSol = np.matrix(([9/190],
                       [28/475],
                       [33/475]))

testA = np.matrix(([5, -2, 3],
                   [-3, 9, 1],
                   [2, -1, -7]))
testX = np.matrix(([0],
                   [0],
                   [0]))
testb = np.matrix(([-1],
                   [2],
                   [3]))
print("Testing iteration methods with the following parameters:")
print("A")
print(testA)
print("x")
print(x_realSol)
print("b")
print(testb)
print('About to Test using Jacobi iteration with 100 iterations and a tolerance = 0.00005')
input('Press any key to continue...')
num_iterations, j_error = jacobi_iter(testA, testb, testX, 100, 0.00005)
print("Finished!")
print("Number of iterations:")
print(num_iterations)
print("The normalized error value:")
print(j_error)
print('Now, I`m aout to test using GS iteration with 100 iterations and a tolerance = 0.00005')
input('Press any key to continue...')
num_iterations, j_error = gs_iter(testA, testb, testX, 100, 0.00005)
print("Finished!")
print("Number of iterations:")
print(num_iterations)
print("The normalized error value:")
print(j_error)


input("Now beginning the 100 random 3x1 matrices trial. Hit a key to continue...")
k = random_three_by_matrix()
max_iteration = 100
print("For GS:")
num_iterations, j_results = gs_iter(s, d, k, max_iteration, .000008)
print("Number of iterations:")
print(num_iterations)
print("The normalized error value:")
print(j_error)


#part d then part c
listRandInitGuess = []
for num in range(100):
    listRandInitGuess.append(random_three_by_matrix())
listJacobiResultIter_y = []
listGSResultIter_y= []
listInitError_Jacobi = []
listInitError_GS = []
Njc_div_Ngs = 0
num_of_Njc_div_Ngs = 0
sumOfXn = np.zeros((3,1))
# Graphing
newJacobiList = [('jacobi result', 'jacobi init error norm')]
newGSList = [[('gs result', 'gs init error norm')]]
for item in listRandInitGuess:
    init_error_norm = norm(item, x_realSol)
    jacobi_result = jacobi_iter(s, d, item, 100, 0.00005)
    if jacobi_result is not None:
        listJacobiResultIter_y.append(jacobi_result[0])
        listInitError_Jacobi.append(init_error_norm)
        newJacobiList.append((jacobi_result[0], init_error_norm))

    GS_result = gs_iter(s, d, item, 100, 0.00005)
    if GS_result is not None:
        listGSResultIter_y.append(GS_result[0])
        listInitError_GS.append(init_error_norm)
        newGSList.append((GS_result[0], init_error_norm))

    if GS_result is not None and jacobi_result is not None:
        Njc_div_Ngs += (jacobi_result[0] / GS_result[0])
        num_of_Njc_div_Ngs += 1

    sumOfXn += item
avg_Njc_div_Ngs = (Njc_div_Ngs / num_of_Njc_div_Ngs)
print("Ratio of [(Jacobi iteration number average) / (GS iteration number average)] = \n" + str(avg_Njc_div_Ngs))
print(" The average solution x_approx:")
avgOfXn = sumOfXn / 100
print(avgOfXn)
print("Average approximate error norm")
avgAppErrNorm = norm(avgOfXn, x_realSol)
print(avgAppErrNorm)

# output to csv
with open('./data/iter_jaboci_data.csv', 'w', newline='') as myfile:
    writer = csv.writer(myfile)
    writer.writerows(newJacobiList)
with open('./data/iter_gs_data.csv', 'w', newline='') as myfile:
    writer = csv.writer(myfile)
    writer.writerows(newGSList)
print("date saved to ./data directory")
print("Part 2 Complete!")