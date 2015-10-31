import numpy as np

# implementation of matrix multiplication method
def matrixMultiply(a, b):
	sizeA = np.shape(a)
	sizeB = np.shape(b)

	#check if inner and outer sizes will work
	if(sizeA[1] != sizeB[0]):
		return null

	iMax = sizeA[0]	# index i is contained by the # of rows of A 
	jMax = sizeB[1] # index j is contained by the # of cols of B 
	numRowsB = sizeB[0]
	rangeI = range(0, iMax)
	rangeJ = range(0, jMax)
	rangeK = range(0, numRowsB)

	# iterate through the matrix and apply matrix multiplicatin logic
	newMatrix = np.zeros((iMax, jMax))
	for i in rangeI:

		for j in rangeJ:
			for k in rangeK:
				newMatrix[i,j] += a[i,k] * b[k, j]
	return newMatrix