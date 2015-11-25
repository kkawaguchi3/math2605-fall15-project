#!/usr/bin/env python
import numpy as np
import modules.problem1_operations as ops
import time

#############
# Part 1 #
#############
#def print_everything():


def A():
    # Part A
    # ######
    print("PART A\n---------\n")
    # testing LU factorization
    print("Testing LU decomposition function `lu_fact`.")
    pascal_size = input("Enter the size of the test Pascal matrix:")
    pascal_size = int(pascal_size)

    P = ops.create_pascal(pascal_size)
    print("Here is your Pascal Matrix:")
    print(P)
    print("I will now factorize using the LU method.")
    input("Press any key to continue")
    L, U, error = ops.lu_fact(P)
    print("L:")
    print(L)
    print("U:")
    print(U)
    print("Error:")
    print(error)
    print("...And that's it!")


def B():
    # Part B
    # ######
    print("PART B\n---------\n")
    print("Testing QR decomposition function `qr_fact_househ`.")
    pascal_size = input("Enter the size of the test Pascal matrix:")
    pascal_size = int(pascal_size)

    P = ops.create_pascal(pascal_size)
    print("Here is your Pascal Matrix:")
    print(P)
    print("I will now factorize using the QR method.")
    Q, R, error = ops.qr_fact_househ(P)
    print("Q:")
    print(Q)
    print("R:")
    print(R)
    print("Error:")
    print(error)
    input("Press any key to continue to Givens method: ")

    print("Testing QR decomposition function `qr_fact_givens`.")
    P = ops.create_pascal(pascal_size)
    print("Here is your Pascal Matrix:")
    print(P)
    print("I will now factorize using the Givens rotation method.")
    input("Press any key to continue")
    Q, R, error = ops.qr_fact_givens(P)
    print("Q:")
    print(Q)
    print("R:")
    print(R)
    print("Error:")
    print(error)
    print("...And that's it!")


def C():
    # Part C
    # ######
    print("PART C\n-------\n")
    print("Solving Ax=b problem using QR and LU methods")

    pascal_size = input("Enter the size of the test Pascal matrix:")
    pascal_size = int(pascal_size)

    P = ops.create_pascal(pascal_size)
    print("Here is your Pascal Matrix:")
    print(P)
    b = ops.create_b(pascal_size)
    print("Here is your b")
    print(b)
    print("I will now solve using LU.")
    input("Press any key to continue")
    x, L, U, error = ops.solve_lu_b(P, b)
    print("L:")
    print(L)
    print("U:")
    print(U)
    print("x:")
    print(x)
    input("Press any key to continue to the Householder method: ")

    print("I will now solve using Householder.")
    x, Q, R, error = ops.solve_qr_b_hh(P, b)
    print("Q:")
    print(Q)
    print("R:")
    print(R)
    print("x:")
    print(x)
    input("Press any key to continue to the Givens method: ")
    print("I will now solve using Givens.")
    x, Q, R, error = ops.solve_qr_b_givens(P, b)
    print("Q:")
    print(Q)
    print("R:")
    print(R)
    print("x:")
    print(x)


def D():

    # Part D
    # ######
    print("PART D\n========\n")
    input("Press any key to initiate testing for LU factorization and generate CSV output")
    ops.save_lu_results()
    input("Press any key to initiate testing for QR Householder factorization and generate CSV output")
    ops.save_hh_results()
    input("Press any key to initiate testing for QR Givens factorization and generate CSV output")
    ops.save_givens_results()
