import numpy as np
#create L and U matrices with all elemets as zero
L=np.array([[0.0 for i in range(3)]for j in range(3)])

#assume Lii=1 all diagonal elements in L matrix as 1
A=np.array([[4,-1,-1],[-1,4,-3],[-1,-3,5]])
b=np.array([[3,-0.5,0]])
b.shape=(3,1)
n=3
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
            elif i>1 and j>i+1:
                temp=A[i][j]
                for k in range(i):
                    temp=temp-(L[i][k]*L[j][k])
                L[i][j]=temp/L[i][i]

print(L)

