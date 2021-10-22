from math import ceil
def f(x,y):
    return -2*x*y**2

x0=0
y0=1
x=0.6
h=0.2
#no of iterations
n=ceil((x-x0)/h)

def rungekutta(x0,y0,h,n):
    while(n!=0):
        k1 = h*f(x0, y0)
        k2 = h*f(x0+(h/2),y0+(k1/2))
        k3 = h*f(x0+(h/2),y0+(k2/2))
        k4 = h* f(x0 + h, y0 + k3)
        y0=y0+(k1+2*k2+2*k3+k4)/6.0
        x0=x0+h
        n=n-1
        print(y0)
    return y0

print("numerical solution of given differential equation at x=0.6:",rungekutta(x0,y0,h,n))