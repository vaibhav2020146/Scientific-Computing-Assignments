#implementing shifting inverse iteration method to find the eigen values and eigen vectors of a matrix closest to a given value:
import numpy as np
import matplotlib.pyplot as plt

def power_method(A):
    count=0
    v=np.array([0,0,1])
    v=v/np.linalg.norm(v)
    v_new=np.dot(A,v)
    v_new=v_new/np.linalg.norm(v_new)
    while np.linalg.norm(v_new-v)>0.0001 and count<1000:
        v=v_new
        v_new=np.dot(A,v)
        v_new=v_new/np.linalg.norm(v_new)
        count+=1
    return v

def shifting_inverse_iteration(A,shift):
    #here shift means the value of the eigen value closest to which we want to find the eigen value and eigen vector
    A_shift=A-shift*np.identity(3)#shifting the matrix
    A_shift_inv=np.linalg.inv(A_shift)#finding the inverse of the shifted matrix
    v=power_method(A_shift_inv)#finding the eigen vector corresponding to the eigen value closest to the shift
    helper=np.dot(np.dot(v,A),v)#finding the eigen value corresponding to the eigen vector
    eigen_value=(1/helper)+shift#finding the eigen value
    #finding eigen vector corresponding to the eigen value: 
    eigen_vector=np.dot(A,v)
    eigen_vector=eigen_vector/np.linalg.norm(eigen_vector)
    print("Eigen value closest to shift:",eigen_value)
    print("Eigen Vector closest to the shift:",eigen_vector)

A = np.array([[6,2,1], [2,3,1],[1,1,1]])
eigen_values,eigen_vectors=np.linalg.eig(A)
print("All Eigen Values:",eigen_values)
print("All Eigen Vectors: ")
print(eigen_vectors)


A_inv=np.linalg.inv(A)
shifting_inverse_iteration(A_inv,2)