import numpy as np
from numpy.lib.twodim_base import eye
#create L and U matrices with all elemets as zero
L=np.array([[0 for i in range(3)]for j in range(3)])
U=np.array([[0 for i in range(3)]for j in range(3)])
#assume Lii=1 all diagonal elements in L matrix as 1
A=np.array([[1,-1,5],[2,-3,1],[1,3,7]])
b=np.array([[5,0,11]])
b.shape=(3,1)
n=3

for i in range(n):
    #L triangular matrix
    for k in range(i,n):
        if k==i:
            L[i][k]=1
        if i>=1:
            L[i][0]=A[i][0]/U[0][0]
        if i>1:
            L[i][1]=(A[i][1]-L[i][0]*U[0][1])/U[1][1]
        if i>2:
            L[i][2]=(A[i][2]-L[i][0]*U[0][1]-L[i][1]*U[1][2])/U[2][2]
        if i>3:
            L[i][3]=(A[i][3]-L[i][0]*U[0][1]-L[i][1]*U[1][2]-L[i][2]*U[2][3])/U[3][3]

    #U triangular matrix
    for j in range(i,n):
        if i==0:
            U[i][j]=A[i][j]
        if i==1 :
            U[i][j]=A[i][j]-L[i][0]*U[0][j]
        if i==2 and j>=2:
            U[i][j]=A[i][j]-L[i][0]*U[0][j]-L[i][1]*U[1][j]
        if i==3 and j>=3:
            U[i][j]=A[i][j]-L[i][0]*U[0][j]-L[i][1]*U[1][j]-L[i][2]*U[2][j]

        if i==4 and j>=4:
            U[i][j]=A[i][j]-L[i][0]*U[0][j]-L[i][1]*U[1][j]-L[i][2]*U[2][j]-L[i][3]*U[3][j]
print("After LUdecomposition")
print("Upper triangular matrix is:")
print(U)
print("Lower triangular matrix is:")
print(L)

#forward substitution
z=np.zeros(len(b))
for i in range(0,len(b),1):
    temp=b[i]
    for j in range(i):
        temp=temp-(L[i][j]*z[j])
    z[i]=temp/L[i][i]
z=z.transpose()

#backward substitution
x=np.zeros(len(b))
for i in range(n-1,-1,-1):
    temp=z[i]
    for j in range(n-1,i,-1):
        temp=temp-U[i][j]*x[j]
    x[i]=temp/U[i][i]
print("Solution to the linear system of equations:")
print(x)