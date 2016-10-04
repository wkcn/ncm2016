#coding=utf-8
import numpy as np

def get_error(t,b):
    return np.sqrt(np.sum((np.power(t - b, 2))))

#列主元
def colE(W, r):
    row,col = W.shape
    maxNum = abs(W[r,r])
    maxNumR = r
    for i in range(r+1, row):
        if abs(W[i,r]) > maxNum:
            maxNum = abs(W[i,r])
            maxNumR = i
    #交换
    q = W[r,:].copy()
    W[r,:] = W[maxNumR, :]
    W[maxNumR, :] = q

#上三角矩阵求解
def uppertri_solve(W):
    row,col = W.shape
    x = np.matrix(np.zeros((row,1)))
    for i in range(row):
        r = row - 1 - i
        q = W[r, -1]
        for c in range(row-i,row):
            q -= W[r,c] * x[c]
        x[r] = q / W[r,r]
    return x

#下三角矩阵求解
def lowertri_solve(W):
    row,col = W.shape
    x = np.matrix(np.zeros((row,1)))
    for r in range(row):
        q = W[r,-1]
        for c in range(r):
            q -= W[r,c] * x[c]
        x[r] = q / W[r,r]
    return x

#消除
def eliminate(W, func = None):
    row,col = W.shape
    for r in range(row):
        if func:
            func(W, r)
        for e in range(r+1, row):
            l = W[e,r] / W[r,r]
            W[e,:] -= l * W[r,:]
    

#高斯消元法
def gauss(A, b, func = None):
    W = np.c_[A, b]
    eliminate(W, func)
    return uppertri_solve(W)

#测试结果误差
def gauss_test(A, b, func = None):
    x = gauss(A,b,func)
    print "x is \n", x
    t = A * x
    print "Testing: A * x = \n", t
    print "Error: ", get_error(t,b)

#LU分解, LU = A
def LU_Decomposition(A):
    W = A.copy()
    row,col = W.shape
    L = np.identity(row)
    for r in range(row):
        for t in range(r+1, row):
            l = W[t,r] / W[r,r]
            W[t,:] -= W[r,:] * l
            L[t,r] = l
    return L, W

#利用LU分解求Ax = b中的x
def LU_Solve(L,U,b):
    '''
    Ax = (LU)x = b
    Ux = y
    Ly = b
    '''
    y = lowertri_solve(np.c_[L, b])
    x = uppertri_solve(np.c_[U, y])
    return x

#利用LU分解求逆矩阵
def LU_Inverse(L, U):
    row,col = L.shape
    I = np.matrix(np.zeros(L.shape))
    for i in range(row):
        b = np.matrix(np.zeros((row, 1)))
        b[i] = 1
        I[:,i] = LU_Solve(L, U, b)
    return I

#追赶法
def chase(A, b):
    row, col = A.shape
    lm = [0. for _ in range(row)] #lm[0] = l_1_0
    li = [0. for _ in range(row)] #li[0] = l_0_0
    u = [0. for _ in range(row)] #u[0] = u_0_1
    li[0] = A[0,0] # l_1_1 = a_1_1
    u[0] = A[0,1] / li[0]
    for i in range(row-1):
        lm[i] = A[i+1,i]
    for i in range(1, row - 1):
        li[i] = A[i,i] - lm[i-1] * u[i-1]
        u[i] = A[i, i+1] / li[i]
    i = row - 1
    li[i] = A[i,i] - lm[i-1] * u[i-1]
    #Ly = b 追
    y = np.matrix(np.zeros((row,1))).astype(np.double)
    y[0] = b[0] / li[0]
    for i in range(1, row):
        y[i] = (b[i] - lm[i-1] * y[i-1]) / li[i]
    #Ux = y 赶
    x = np.matrix(np.zeros((row,1))).astype(np.double)
    x[-1] = y[-1]
    for i in range(row - 2, -1, -1):
        x[i] = y[i] - u[i] * x[i+1]
    return x

def iteration_solve(method_mask, A, b, x0, max_error, max_iter_num = -1):
    x = x0.copy()
    row, col = A.shape
    iter_num = 0
    last_error = 0
    while True:
        if max_iter_num != -1:
            if iter_num >= max_iter_num:
                print "iteration end, iter_num >= max_iter_num"
                break
        iter_num += 1

        #雅可比迭代法
        def Jacobi_Method():
            oldx = x.copy()
            for i in range(row):
                s = 0.
                for j in range(row):
                    if i != j:
                        s += A[i, j] * oldx[j]
                x[i] = (b[i] - s) / A[i,i]

        #高斯-塞德尔迭代法
        def Gauss_Seidel_Method():
            for i in range(row):
                s = 0.
                for j in range(row):
                    if i != j:
                        s += A[i, j] * x[j]
                x[i] = (b[i] - s) / A[i,i]

        if method_mask == "J":
            Jacobi_Method()
        elif method_mask == "G" or method_mask == "S":
            Gauss_Seidel_Method()
        else:
            print "Error! Please use right method name"
            break

        error = get_error(A * x, b)
        print "iter: ", iter_num, " error: ", error
        #print x
        if error == last_error:
            print "iteration finished, current error is same as last_error"
            break
        last_error = error
        if error <= max_error:
            print "iteration finished, error <= max_error"
            break
    return x


