import math
#coverting given system of euations into diagonally dominant.
x0=0
y0=0
z0=0
n=5
x1=[]
y1=[]
z1=[]
while(n!=0):
    x=(12.6-2*y0-2*z0)/26
    x1.append(x)
    y=(-14.3-3*x0-z0)/27
    y1.append(y)
    z=(6-2*x0-3*y0)/17
    z1.append(z)
    x0=x
    y0=y
    z0=z
    n=n-1
for i in range(len(x1)-1):
    t=x1[i+1]-x1[i]
    r=y1[i+1]-y1[i]
    s=z1[i+1]-z1[i]
    if (t<0.00001):
        x=x1[i+1]
    if (r<0.00001):
        y=y1[i+1]
    if (s<0.00001):
        z=z1[i+1]

print("Solution of linear system of equations: x:{},y:{},z:{}".format(x,y,z))









