import numpy as np

#implementing gaussian elimination with no pivoting
def gaussian_elimination(A,b):
    n=len(b)
    for k in range(n-1):
        for i in range(k+1,n):
            if A[k,k]!=0.0:
                for j in range(k+1,n):
                    A[i,j]=A[i,j]-A[i,k]*A[k,j]/A[k,k]
                b[i]=b[i]-A[i,k]*b[k]/A[k,k]
    return A,b

#implementing back substitution
def back_substitution(A,b):
    n=len(b)
    x=np.zeros(n)
    x[n-1]=b[n-1]/A[n-1,n-1]
    for i in range(n-2,-1,-1):
        if A[i,i]!=0.0:
            x[i]=(b[i]-np.dot(A[i,i+1:n],x[i+1:n]))/A[i,i]
    return x
    
#error from un-pivoted gaussian elimination
def error(A,b,x):
    return np.linalg.norm(np.dot(A,x)-b)#by default it have a 2nd norm

#residual from un-pivoted gaussian elimination
def residual(A,b,x):
    return np.linalg.norm(np.dot(A,x)-b)/np.linalg.norm(b)#for 2nd norm



