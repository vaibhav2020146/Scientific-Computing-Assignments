import numpy as np
import matplotlib.pyplot as plt
error=[]
def Reyleigh_quotient_iteration(A):
    #choosing arbitary non zero vector
    x=np.array([1,1,1])
    for i in range(1000):
        #computing shift
        shift=x.T.dot(A).dot(x)/x.T.dot(x)
        #computing the inverse of the matrix
        A_inv=np.linalg.inv(A-shift*np.identity(A.shape[0]))
        #computing the new vector
        x=A_inv.dot(x)
        x=x/np.linalg.norm(x)
        #computing the error
        #error.append(np.linalg.norm(A.dot(x)-shift*x))
        #estimate the error as difference true eigen value and the eigen value computed using Reyleigh quotient iteration:
        error.append(np.linalg.norm(eigen_values[0]-shift))



    #computing the eigen value
    eigen_value=x.T.dot(A).dot(x)/x.T.dot(x)
    #computing the eigen vector
    eigen_vector=x
    return eigen_value,eigen_vector

A = np.array([[2,3,2], [10,3,4],[3,6,1]])

eigen_values,eigen_vectors=np.linalg.eig(A)
print("All eigen values",eigen_values)
print("All eigen vectors")
print(eigen_vectors)

eigen_value_by_function,eigen_vector_by_function=Reyleigh_quotient_iteration(A)
print("Largest eigen value obtained by function",eigen_value_by_function)
print("Largest eigen vector obtained by function",eigen_vector_by_function)

#print(error)
#plt.plot(error)
#plt.show()
#rate of convergence of the method
print("Rate of convergence:",np.log(np.abs(eigen_value_by_function-eigen_values[0]))/np.log(np.linalg.norm(eigen_vector_by_function-eigen_vectors[:,0])))#log is used to avoid the overflow error
