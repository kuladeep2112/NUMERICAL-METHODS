import numpy as np
#create L and U matrices with all elemets as zero
L=np.array([[0.0 for i in range(4)]for j in range(4)])

#assume Lii=1 all diagonal elements in L matrix as 1
A=np.array([[1.44,-0.36, 5.52, 0.00],[-0.36,10.33,-7.78,0],[5.52,-7.78,28.40,9],[0,0,9,61]])
b=np.array([[3,-0.5,0]])
b.shape=(3,1)
n=4
#check if given matrix is symmetic or not
B=A.transpose()

if np.array_equal(A,B):
    print("MATRIX is symmetric")
    #lower triangular matrix
    for i in range(n):
        for j in range(i,n):
            if i==j :
                temp=A[i][j]
                print(temp)
                for k in range(i):
                    temp=temp-(L[i][k])**2
                    print(temp)
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
                print(temp)
                for k in range(i):
                    temp=temp-(L[i][k]*L[j][k])
                    print(temp)
                L[j][i]=temp/L[i][i]
                print(L[i][j])
LT=L.transpose()
print(np.matmul(L,LT))

