#coding=utf-8
from mathlib import *

def ques1():
    A = np.matrix([[1,2,3],
                   [0,1,2],
                   [2,4,1]]).astype(np.double)
    b = np.matrix([14,8,13]).T.astype(np.double)
    print "Ax = b"
    print "A = \n", A
    print "b = \n", b
    gauss_test(A, b, colE)

def ques2():
    A = np.matrix([[2,1,-2,0],
                   [4,0,-1,3],
                   [0,3,2,-2],
                   [1,1,0,5]]).astype(np.double)
    Abackup = A.copy()
    print A
    print "Taking Column principal component Gaussian elimination method:"
    eliminate(A, colE)
    print A
    s = 1
    for i in range(A.shape[0]):
        s *= A[i, i]
    print "so, det(A) = ", s
    print "Checking, numpy.det(A) = ", np.linalg.det(Abackup)

def ques3_test(A, b):
    print "Ax = b"
    print "A = \n", A
    print "b = \n", b
    print "Taking Column principal component Gaussian elimination method:"
    gauss_test(A,b,colE)
    print "Don't Take Column principal component Gaussian elimination method:"
    gauss_test(A,b,None)

def ques3():
    A = np.matrix([[0.3*1e-15, 59.14, 3, 1],
                   [5.291, -6.130, -1, 2],
                   [11.2,9,5,2],
                   [1,2,1,1]]).astype(np.double)
    b = np.matrix([59.17,46.78,1,2]).T.astype(np.double)
    ques3_test(A, b)

    A = np.matrix([[10,-7,0,1],
                   [-3,2.099999,6,2],
                   [5,-1,5,-1],
                   [0,1,0,2]]).astype(np.double)
    b = np.matrix([8,5.909901,5,1]).T.astype(np.double)
    ques3_test(A,b)

while True:
    print "Please Input a Number to Get Answer"
    print "1: Ques1"
    print "2: Ques2"
    print "3: Ques3"
    print "q: Quit"
    i = raw_input("")
    if i == 'q' or i == 'Q':
        break
    if len(i) == 1 and i >= '1' and i <= '3':
        eval("ques%s()" % i)
    else:
        print "Error"
