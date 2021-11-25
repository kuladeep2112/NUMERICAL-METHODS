import numpy as np
import math
A=np.array([[1,2,0],[0,1,1],[1,0,1]])
R=np.array([[0.0 for i in range(3)]for j in range(3)])
Q=np.array([[0.0 for i in range(3)]for j in range(3)])

for i in range(len(A)):
    sum=0
    for j in range(i+1):
        if i!=j:
            print(i+1,j+1)
            print(A[:,i])
            R[j][i]=np.matmul(np.transpose(Q[:,j]),A[:,i])
            print(j+1,i+1,R[j][i])
            print(Q[:,j])
            sum=sum+R[j][i]*Q[:,j]
    v=A[:,i]-sum
    R[i][i]=np.linalg.norm(v)
    Q[:,i]=v/R[i][i]
print(np.round_(Q, decimals = 10))
print(np.round_(R, decimals = 10))
print(np.round_(np.matmul(Q,R),decimals=10))