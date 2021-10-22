from math import ceil
import math
def f(x):
    # return math.cos(x)-math.sin(x) #question1 x[0,1]
    # return math.cos(x) - x * math.exp(x)
     return x**3-3*x+1 #x[1.5,2] #question2

a=0
b=1
temp=0
#finding root nearest to 0.001 accuracy
while (temp==0):

    print(a,b)
    t=f(b)-f(a)
    z=a*f(b)-b*f(a)
    x=z/t


    if f(a)<0 and f(x)>0:
        b=x

    elif f(b)>0 and f(x)<0:
        a=x

    elif f(a)>0 and f(x)<0:
        b=x

    elif f(b)<0 and f(x)>0:
        a=x

    t=f(b)-f(a)
    z=a*f(b)-b*f(a)
    x1=float(z/t)
    print(abs(x1-x))
    if abs(x1-x)<0.001:
        temp=1


print("root of the equation:",x)