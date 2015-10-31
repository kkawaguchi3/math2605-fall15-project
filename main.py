#!/usr/bin/env python
import os
import sys
import numpy as np
import modules.matrixOperations as mo


if __name__ == '__main__':
	print ('It works!')
matrixA = np.matrix([[1,2], [2,1], [2,1]])
matrixB = np.matrix([[3,2,1], [2,1,1]])
answer = mo.matrixMultiply(matrixA, matrixB)
print(answer)