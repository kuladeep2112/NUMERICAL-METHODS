from math import ceil
def f(x,y):
    return -2*x*y**2

x0=0
y0=1
x=0.6
h=0.2
#no of iterations
n=ceil((x-x0)/h)

def Euler(x0,y0,h,n):
    while(n!=0):
        k1 = x0+.5*h
        k2 = y0+.5*h*f(x0,y0)
        y0=y0+h*f(k1,k2)
        x0=x0+h
        n=n-1
        print(y0)
    return y0

print("numerical solution of given differential equation at x=0.6:",Euler(x0,y0,h,n))