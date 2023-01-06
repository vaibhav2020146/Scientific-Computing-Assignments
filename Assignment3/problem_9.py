import numpy as np
import matplotlib.pyplot as plt

def QR_iteration1(A):
    Q,R=np.linalg.qr(A)
    while np.linalg.norm(Q-np.identity(A.shape[0]))>2:#instead of it we can also run a loop for a fixed number of iterations
        #choosing shift as the corner entry
        shift=A[A.shape[0]-1,A.shape[0]-1]
        #finding the QR decomposition of the matrix
        Q,R=np.linalg.qr(A-shift*np.identity(A.shape[0]))
        #finding the new matrix
        A=np.dot(R,Q)+shift*np.identity(A.shape[0])
    #now we will find the eigen values and eigen vectors of the matrix
    eigen_values=np.diag(A)#diagonal elements of the matrix are the eigen values
    eigen_vectors=Q#eigen vectors are the columns of the matrix Q
    return eigen_values,eigen_vectors

A = np.array([[6,2,1], [2,3,1],[1,1,1]])
eigen_values,eigen_vectors=QR_iteration1(A)
print("All Eigen value:",eigen_values)
print("All Eigen vector",eigen_vectors)