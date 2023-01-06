import numpy as np
import matplotlib.pyplot as plt

#reading data from the file
t=[]
y=[]
with open("C://Users//91991//Desktop//SC//hw2_data_ty.txt") as f:
    for line in f:
        t.append(float(line.split()[0]))
        y.append(float(line.split()[1]))
#now using t and y to solve linear least square problem 
#defining the matrix A
A=np.zeros((len(t),2))
for i in range(len(t)):
    A[i][0]=t[i]#alpha
    A[i][1]=1#beta

#now solving using np.linag.solve
x1=np.linalg.solve(A.T@A,A.T@y)
print(x1)
#computting the error in the fit that is the 2nd norm of the residual using:
residual=np.linalg.norm(A@x1-y)#when norm is not given it is 2nd norm
print(residual)
#now plotting the data
plt.figure()
plt.plot(t, y, 'bo', ms=2.5)
plt.plot(t,np.exp(x1[0]*np.array(t)+x1[1])/(1+np.exp(x1[0]*np.array(t)+x1[1])),'g')
plt.grid(True)
plt.xlabel("$t_i$", fontsize=14)
plt.ylabel("$f(t_i)$", fontsize=14)
plt.gcf().tight_layout()
plt.show()



#now solving the linear least square problem
x=np.linalg.lstsq(A,y,rcond=None)[0]
print(x)
#computting the error in the fit that is the 2nd norm of the residual
residual=np.linalg.lstsq(A,y,rcond=None)[1]
print(residual)
#now plotting the data
plt.figure()
plt.plot(t, y, 'bo', ms=2.5)
plt.plot(t,np.exp(x[0]*np.array(t)+x[1])/(1+np.exp(x[0]*np.array(t)+x[1])),'r')
plt.grid(True)
plt.xlabel("$t_i$", fontsize=14)
plt.ylabel("$f(t_i)$", fontsize=14)
plt.gcf().tight_layout()
plt.show()


#now plotting both the fits in the same plot
plt.figure()
plt.plot(t, y, 'bo', ms=2.5)
plt.plot(t,np.exp(x[0]*np.array(t)+x[1])/(1+np.exp(x[0]*np.array(t)+x[1])),'r')
plt.plot(t,np.exp(x1[0]*np.array(t)+x1[1])/(1+np.exp(x1[0]*np.array(t)+x1[1])),'g')
plt.grid(True)
plt.xlabel("$t_i$", fontsize=14)
plt.ylabel("$f(t_i)$", fontsize=14)
plt.gcf().tight_layout()
plt.show()
