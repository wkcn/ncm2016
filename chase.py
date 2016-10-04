#coding=utf-8
import numpy as np
from mathlib import *

def GetAb(n):
    A = np.matrix(np.zeros((n,n))).astype(np.double)
    b = np.matrix(np.ones((n,1))).astype(np.double) * -5
    b[0] = -7
    A[0,0] = 2
    A[-1,-1] = 2
    A[0,1] = 1
    A[-1,-2] = 1
    for r in range(1, n - 1):
        A[r, r - 1] = 1
        A[r, r] = 2
        A[r, r + 1] = 1
    return A,b

A,b = GetAb(5)
print "Ax = b"
print "A = "
print A
print "b = "
print b
'''
A = np.matrix("2,-1,0,0;-1,2,-1,0;0,-1,2,-1;0,0,-1,2").astype(np.double)
b = np.matrix("1;0;0;1").astype(np.double)
'''
print "Chasing method"
x = chase(A, b)
print "x = "
print x
print "Error: ", get_error(A * x, b)

print ""

print "LU method"
L,U = LU_Decomposition(A)
x = LU_Solve(L, U, b)
print "x = "
print x
print "Error: ", get_error(A * x, b)
