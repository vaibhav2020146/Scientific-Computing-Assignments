import numpy as np
from scipy.linalg import solve_triangular


#b-part
for k in range (6,16):
    A=np.array([[1,1],[10**(-k),0],[0,10**(-k)]])
    b=np.array([1,1+10**(-k),1-10**(-k)])
    #solve the linear least squares problem using QR factorization of A
    Q,R=np.linalg.qr(A)
    y=np.dot(Q.T,b)
    x=np.linalg.solve(R,y)
    print("Solution using QR factorization of A is for k=",k,"is",x)
    #solve the linear least squares problem using triangular of scipy
    x=solve_triangular(R,y,lower=False)
    print("Solution using Triangular Solver of A is for k=",k,"is",x)

print()
#c-part
for k in range (6,16):
    A=np.array([[1,1],[10**(-k),0],[0,10**(-k)]])
    b=np.array([1,1+10**(-k),1-10**(-k)])
    #solve the linear least squares problem using normal equations A.T*A*x=A.T*b
    x=np.linalg.solve(np.dot(A.T,A),np.dot(A.T,b))
    #getting singular matrix for higher k values because it is approaching to zero so the matrix is not invertible
    print("Solution using normal equations of A is for k=",k,"is",x)