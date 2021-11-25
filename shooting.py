from math import ceil
def f(z):
    return z
def g(x,y):
    return 6*(y**2)-x

x0=0
y0=1 # boundary values
y1=5
x=1
h=0.3333
z0=1.2# initial slopes
z1=1.5
#no of iterations
n=round((x-x0)/h)
Max_iter=10

def Euler(x0,y0,z0,h,n):
    while(n!=0):
        ytemp=y0
        y0=y0+h*f(z0)
        z0=z0+h*(g(x0,ytemp))
        x0=x0+h
        n=n-1
    return y0
a=z0
b=z1

while(Max_iter!=0):
    t=Euler(x0,y0,a,h,n)
    O_a=t-5
    if abs(O_a)<=0.001:
        print("Solution is :",a)
        break
    t1=t=Euler(x0,y0,b,h,n)
    O_b=t1-5
    if abs(O_b)<=0.001:
        print("Solution is :",b)
        break
    #secent method formula
    #z2 is new root
    z2=b-((b-a)/(O_b-O_a))*O_b
    t2=Euler(x0,y0,z2,h,n)
    if abs(t2-5)<=0.001:
        print("Solution is :",z2)
        break
    a=b
    b=z2
    O_a=O_b
    O_b=t2-5
    Max_iter-=1