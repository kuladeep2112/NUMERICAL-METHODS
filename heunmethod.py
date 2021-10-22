from math import ceil

def f(x,y):
    return -2*x*y**2

x0=0
y0=1
x=0.6
h=0.2
#no of iterations
n=ceil((x-x0)/h)

def Heun_m(x0,y0,h,n):
    while(n!=0):
        n=n-1
        t=f(x0,y0)
        y1=y0+h*f(x0,y0)
        x1=x0+h
        x0=x1
        y0=y0+0.5*h*(t+f(x1,y1))
        print(y0)
    return y0

print("numerical solution of given differential equation ",Heun_m(x0,y0,h,n))