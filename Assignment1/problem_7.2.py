import math

val=0.0
for i in range(1,5001):
    val+=1/i
    if(i%100==0):
        helper=val
        helper-=math.log(i+(1/2))
        print("Value at i=",i,helper)
