import numpy as np
import math as mt

for i in range(21):
    x=(mt.pi/4)+(2*(mt.pi)*(10**i))
    print("(x, tan(x)) = (%1.16f, %1.16f)"%(x, np.tan(x))) 

print()

#finding relative condition number as:
#|(x*(f'(x))/f(x))=|(x*(1/tan(x)+tan(x)))|

for i in range(21):
    x=(mt.pi/4)+(2*(mt.pi)*(10**i))
    #finding relative condition number considering x as input
    print("Relative condition number = %1.16f"%(abs(x*( (1/np.tan(x)) + (np.tan(x) )))))