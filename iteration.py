#coding=utf-8
import numpy as np
from mathlib import *

def get_A(n):
    A = np.matrix(np.zeros((n,n))).astype(np.double)
    A[0,0] = 3.
    A[0,1] = - 1. / 2
    A[0,2] = - 1. / 4

    A[1,0] = - 1. / 2
    A[1,1] = 3.
    A[1,2] = - 1. / 2
    A[1,3] = - 1. / 4

    A[-2,-4] = - 1. / 4
    A[-2,-3] = - 1. / 2
    A[-2,-2] = 3.
    A[-2,-1] = - 1. / 2

    A[-1, -3] = - 1. / 4
    A[-1, -2] = - 1. / 2
    A[-1, -1] = 3.

    for i in range(2, n - 2):
        A[i, i - 2] = - 1. / 4
        A[i, i - 1] = - 1. / 2
        A[i, i] = 3.
        A[i, i + 1] = - 1. / 2
        A[i, i + 2] = - 1. / 4 
    return A

def get_A_b_x0(n):
    A = get_A(n)
    b = np.matrix(np.zeros((n,1))).astype(np.double)
    b[0] = 1
#b = np.matrix(np.random.random((n,1))) * 100
    x0 = np.matrix(np.zeros((n,1))).astype(np.double)
    return A,b,x0

def ques1():
    n = 20
    A,b,x0 = get_A_b_x0(n)

    '''
    A = np.matrix("10,-1,-2;-1,10,-2;-1,-1,5").astype(np.double)
    b = np.matrix("7.2;8.3;4.2");
    x0 = np.matrix("0.;0.;0.")
    '''

    print "Jacobi_Method"
    x1 = iteration_solve("J", A, b, x0, 1e-14, 1000)
    print ""
    print "Gauss_Seidel_Method"
    x2 = iteration_solve("G", A, b, x0, 1e-14, 1000)

def ques2():
    n = 20
    ratio = 3
    A,b,x0 = get_A_b_x0(n)
    for i in range(n):
        A[i, i] *= ratio
    print "Jacobi_Method"
    x1 = iteration_solve("J", A, b, x0, 1e-14, 1000)

def ques3():
    ratio = 1
    A = np.matrix("6,2,-1;1,4,-2;-3,1,4").astype(np.double)
    b1 = np.matrix("-3;2;4").astype(np.double)
    b2 = np.matrix("100;-200;345").astype(np.double)
    x0 = np.matrix(np.zeros(b1.shape)).astype(np.double)
    for i in range(A.shape[0]):
        A[i, i] *= ratio
    print "Jacobi_Method"
    print "Ax = b1"
    x1 = iteration_solve("J", A, b1, x0, 1e-14, 1000)
    print x1
    print "Ax = b2"
    x2 = iteration_solve("J", A, b2, x0, 1e-14, 1000)
    print x2

def ques4():
    ratio = 1
    A = np.matrix("1,3;-7,1").astype(np.double)
    b = np.matrix("4;-6").astype(np.double)
    x0 = np.matrix(np.zeros(b.shape)).astype(np.double)
    for i in range(A.shape[0]):
        A[i, i] *= ratio
    print "Jacobi_Method"
    x1 = iteration_solve("J", A, b, x0, 1e-14, 1000)
    print x1
    
ques4()
