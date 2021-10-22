def f(x):
    return x**2-4*x-7
def diff(x):
    return 2*x-4

#initial root
x0=5
temp=0
while(temp==0):
    h=f(x0)/diff(x0)
    x1=x0-h
    if abs(x1-x0) < 0.001:
        temp=1
    x0=x1
print(x0)

