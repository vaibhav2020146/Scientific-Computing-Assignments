import numpy as np
import matplotlib.pyplot as plt

def forward(f, x, h):
    return (f(x+h)-f(x))/h

def function(x):
    return np.exp(-np.sin(x**3)/4)

def exact_derivative(x):
    return -3/4*np.cos(x**3)*x**2*np.exp(-np.sin(x**3)/4) 
h=[]
for i in range(1, 16):
    h.append(10**(-i))
#print(h)
errors=[]
for i in range(len(h)):
    y = forward(function,1, h[i])
    error = np.abs(y-exact_derivative(1))/exact_derivative(1)
    print('h =', h[i])
    #find absolute error
    print('Absolute error =', abs(error))
    errors.append(abs(error))
    #find relative error

#plotting the relative error on log-log scale:
plt.loglog(h, errors, 'b-')
#labeling the axes
plt.xlabel('h')
plt.ylabel('error')
plt.show()