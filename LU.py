#coding=utf-8
import numpy as np
from mathlib import *

def GetAb(n):
    A = np.matrix(np.zeros((n,n))).astype(np.double)
    b = np.matrix(np.zeros((n,1))).astype(np.double)
    b[0,0] = 1
    for r in range(n):
        k = n - r
        for c in range(r+1):
            A[r,c] = k
            k += 1
    return A,b

n = 3
def set_n():
    global n
    try:
        n = int(raw_input("Please Input n: "))
    except:
        print "Input Error, Please Set N Again"
        print "" 
        set_n()

set_n()
A,b = GetAb(n) 
print "A = "
print A
print "b = "
print b

def ques1():
    L,U = LU_Decomposition(A)
    print "L = "
    print L
    print "U = "
    print U

def ques2():
    #(1)
    print "Ax = b"
    L,U = LU_Decomposition(A)
    x = LU_Solve(L,U,b) 
    print "x = "
    print x
    print "Error: ", get_error(A * x, b)
    #(2)
    print "(A^2)x = b"
    A2 = A ** 2
    x = b.copy()
    for i in range(2):
        x = LU_Solve(L,U,x)
    print "x = "
    print x
    print "Error: ", get_error(A2 * x, b)
    #(3)
    print "(A^3)x = b"
    A3 = A ** 3
    x = b.copy()
    for i in range(3):
        x = LU_Solve(L,U,x)
    print "x = "
    print x
    print "Error: ", get_error(A3 * x, b)
    #LM = A^3
    print "LM = A^3, LMx = b"
    L3, M3 = LU_Decomposition(A3)
    x = LU_Solve(L3, M3, b)
    print "x = "
    print x
    print "Error: ", get_error(A3 * x, b)

def ques3():
    L,U = LU_Decomposition(A)
    I = LU_Inverse(L, U)
    print "Inverse matrix of A: "
    print I
    print "Error: ", get_error(I * A, np.identity(I.shape[0]))

def ques4():
    A = np.matrix([[4,2,1,5],
                   [8,7,2,10],
                   [4,8,3,6],
                   [12,6,11,20]]).astype(np.double)
    L, U = LU_Decomposition(A)
    print "A = "
    print A
    print "L = "
    print L
    print "U = "
    print U
    print "Error: ", get_error(L * U, A)
    

while True:
    print ""
    print "Please Input a Number to Get Answer"
    print "1: Ques1 Get L, U"
    print "2: Ques2 LU to solve equations"
    print "3: Ques3 Get inverse matrix of A"
    print "4: Ques4 LU_Decomposition"
    print "q: Quit"
    i = raw_input("")
    if i == 'q' or i == 'Q':
        break
    if len(i) == 1 and i >= '1' and i <= '4':
        eval("ques%s()" % i)
    else:
        print "Input Error"
