import numpy as np
#create L and U matrices with all elemets as zero
L=np.array([[0.0 for i in range(5)]for j in range(5)])

#assume Lii=1 all diagonal elements in L matrix as 1
A=np.array([[2,-1,0,0,0],[-1,2,-1,0,0],[0,-1,2,-1,0],[0,0,-1,2,-1],[0,0,0,-1,2]])
b=np.array([[5,-5,4,-5,5]])
b.shape=(5,1)
n=5
#check if given matrix is symmetic or not
B=A.transpose()

if np.array_equal(A,B):
    print("MATRIX is symmetric")
    #lower triangular matrix
    for i in range(n):
        for j in range(i,n):
            if i==j :
                temp=A[i][j]
                for k in range(i):
                    temp=temp-(L[i][k])**2
                L[i][j]=np.sqrt(temp)
            elif i==0 and j>0:
                L[j][i]=A[i][j]/L[i][i]
            elif i==1 and j>1:
                t=L[i][0]
                temp=A[i][j]
                temp=temp-(t*L[j][0])
                L[j][j-1]=temp/L[i][i]
            elif i>1 and j>=i+1:
                temp=A[i][j]
                for k in range(i):
                    temp=temp-(L[i][k]*L[j][k])
                L[j][i]=temp/L[i][i]

LT=L.transpose()
print("Lower Triangular Matrix")
print(L)
print("Upper Triangular Matrix")
print(LT)
LT=L.transpose()
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
        temp=temp-LT[i][j]*x[j]
    x[i]=temp/LT[i][i]
print("Solution to the linear system of equations:")
print(x)

