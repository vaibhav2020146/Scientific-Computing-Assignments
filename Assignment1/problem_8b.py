import numpy as np

#implementing gaussian elimination with pivoting
def gaussian_elimination_pivoting(A,b):
    n=len(b)
    for k in range(n-1):
        #pivoting
        p=np.argmax(abs(A[k:n,k]))+k
        if p!=k:
            A[[k,p]]=A[[p,k]]
            b[[k,p]]=b[[p,k]]
        for i in range(k+1,n):
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
        x[i]=(b[i]-np.dot(A[i,i+1:n],x[i+1:n]))/A[i,i]
    return x

#error from pivoted gaussian elimination
def error_pivoting(A,b,x):
    return np.linalg.norm(np.dot(A,x)-b,np.inf)

#residual from pivoted gaussian elimination
def residual_pivoting(A,b,x):
    return np.linalg.norm(np.dot(A,x)-b)/np.linalg.norm(b)

