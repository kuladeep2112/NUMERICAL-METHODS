import numpy as np
#create L and U matrices with all elemets as zero
A=np.array([[3.5,2.77,-0.76,1.8],[-1.8,2.68,3.44,-0.09],[0.27,5.07,6.9,1.61],[1.71,5.45,2.68,1.71]])
b=np.array([7.31,4.23,13.85,11.55])
b=b.transpose()
n=A.shape[0]

L=np.eye(n)
U=np.copy(A)
for i in range(n):
    p=U[i][i]
    for j in range(i+1,n):
        L[j][i]=U[j][i]/p

        U[j]=U[j]-L[j][i]*U[i]
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
print(np.matmul(L,U))
print(np.matmul(A,x))