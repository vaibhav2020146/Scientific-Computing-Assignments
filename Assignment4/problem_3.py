import numpy as np
import matplotlib.pyplot as plt

#function to compute the Lagrange interpolation polynomial
def lagrange(x, xdata, ydata):
    n = len(xdata)
    y = np.zeros(len(x))
    for i in range(n):
        p = np.ones(len(x))
        for j in range(n):
            if j != i:
                p = p*(x-xdata[j])/(xdata[i]-xdata[j])
        y = y + ydata[i]*p
    return y

#function to compute the cubic spline interpolant:
def spline(x, xdata, ydata):
    n = len(xdata)
    y = np.zeros(len(x))
    for i in range(n-1):
        p = np.ones(len(x))
        for j in range(n-1):
            if j != i:
                p = p*(x-xdata[j])/(xdata[i]-xdata[j])
        y = y + ydata[i]*p
    return y

#function to compute the runge function
def runge(x):
    return 1/(1+25*(x**2))

#number of data points
n = 21#change it to 11,21 as given in the pdf

#data points
xdata = np.linspace(-1,1,n)
ydata = runge(xdata)

#points to evaluate the interpolant
x = np.linspace(-1,1,100)#here 100 is the number of points and -1 to 1 is the interval, for points to be equally spaced in the interval -1 to 1 set x = np.linspace(-1,1,1000)

#compute polynomial interpolant
y = lagrange(x, xdata, ydata)

#plot interpolant and runge function
plt.plot(x, y, 'b-', xdata, ydata, 'ro', x, runge(x), 'g-')
plt.legend(['interpolant', 'data points', 'runge function'])
plt.show()

#computing the cubic spline interpolant
y = spline(x, xdata, ydata)

#plot interpolant for cubic spline:
plt.plot(x, y, 'b-', xdata, ydata, 'ro', x, runge(x), 'g-')
plt.legend(['interpolant', 'data points', 'runge function'])
plt.show()