import numpy as np
import matplotlib.pyplot as plt

def power_method(A):
    v=np.array([0,0,1])#starting vector
    v=v/np.linalg.norm(v)#normalizing the vector
    v_new=np.dot(A,v)#finding the new vector
    v_new=v_new/np.linalg.norm(v_new)#normalizing the vector
    while np.linalg.norm(v_new-v)>0.0001:#checking the convergence
        v=v_new#updating the vector
        v_new=np.dot(A,v)#finding the new vector
        v_new=v_new/np.linalg.norm(v_new)
    return v_new

def inverse_iteration(A):
    x=np.array([0,0,1])
    for i in range(100):
        x=np.dot(np.linalg.inv(A),x)#finding the new vector
        x=x/np.linalg.norm(x)#normalizing the vector
    return -1*x
A = np.array([[2,3,2], [10,3,4],[3,6,1]])
v=power_method(A)
print("Eigen Vector corresponding to largest Eigen Value:",v)
largest_eigen_value=np.dot(np.dot(v,A),v)
print("Largest Eigen Value:",largest_eigen_value)


#finding the smallest eigen value of a matrix by taking the inverse of the matrix and then applying power method and the value should be smallest in ters of it's magnitude:
A = np.array([[2,3,2], [10,3,4],[3,6,1]])
A_inv=np.linalg.inv(A)
v=inverse_iteration(A)
print("Eigen Vector corresponding to smallest Eigen Value(in terms of magnitude):",v)
smaallest_eigen_value=(np.dot(np.dot(v,A),v))
print("Smallest Eigen value (in terms of magnitude):",abs(smaallest_eigen_value))


#find all eigen values and eigen vectors of a matrix using numpy.linalg.eig
eigen_values,eigen_vectors=np.linalg.eig(A)
print("All Eigen Values:",eigen_values)
print("All Eigen Vectors: ")
print(eigen_vectors)