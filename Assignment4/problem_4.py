import numpy as np
import matplotlib.pyplot as plt

def composite(f, a, b, n):
    h = (b-a)/n
    x = np.linspace(a,b,n+1)
    y = f(x)
    s = y[0] + y[n]
    for i in range(1,n):
        s = s + 2*y[i]
    return h*s/2

#function for testing would be 3∫1 (100/x)*sin (10x) dx.:
def function(x):
    return (100/x)*np.sin(10/x)

#number of subintervals
#n = 64
various_n = [2,4, 8, 16, 32, 64]
for n in various_n:
    #compute integral
    I = composite(function, 1, 3, n)

    #exact value of the integral
    Iexact = np.arctan(1)

    #absolute error
    error = np.abs(I-Iexact)

    #relative error
    error = error/Iexact

    #print results
    print('n =', n)
    print('I =', I)
    print('Iexact =', Iexact)
    print('Absolute error =', error)
    print('Relative Error =', error*100, '%')
